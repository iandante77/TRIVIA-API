import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10
def paginate_questions(request,selection):
    page=request.args.get('page',1,type=int)  
    start=(page-1)* QUESTIONS_PER_PAGE
    end=start+QUESTIONS_PER_PAGE
    questions=[book.format() for book in selection]
    current_questions=questions[start:end]
    return current_questions

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response

    @app.route('/categories')
    def get_categories():
        all_categories = Category.query.all()
        categories = {}
        try:
            for category in all_categories:
                categories[category.id] = category.type
            return jsonify({
                'success': True,
                'categories': categories
            })
        except:
            abort(404)


    @app.route('/questions')
    def get_questions():
        selection = Question.query.order_by(Question.id).all()
        all_questions = paginate_questions(request, selection)
        try:
            if len(all_questions) == 0:
                abort(404)
            all_categories = Category.query.all()
            categories = {}
            for category in all_categories:
                categories[category.id] = category.type
        

            return jsonify({
                'success': True,
                'questions': all_questions,
                'total_questions': len(Question.query.all()),
                'categories': categories
            })
        except:
            abort(404)

    
    @app.route("/questions/<int:question_id>", methods=["DELETE"])
    def delete_question(question_id):
        question = Question.query.get(question_id)
        if question is None:
            abort(404)
        try:
            question.delete()
            return jsonify({"success": True})
        except:
            abort(422)
    
    @app.route('/questions', methods=['POST'])
    def add_question():
        body=request.get_json()
        new_question = body.get('question')
        new_answer = body.get('answer')
        new_difficulty = body.get('difficulty')
        new_category = body.get('category')
        search = body.get("searchTerm")
        if search:
            selection =  Question.query.filter(Question.question.ilike("%{}%".format(search))).all()
            all_questions = paginate_questions(request, selection)

            return jsonify({
            'success': True,
            'questions': all_questions,
            'total_questions': len(selection)
            })

        try:
            question=Question(question=new_question, answer=new_answer, difficulty=new_difficulty,category=new_category)
            question.insert()
            selection=Question.query.order_by(Question.id).all()
            page_questions=paginate_questions(request,selection)
            return jsonify({
                'success':True,
                'created':question.id,
                'question':page_questions,
                'total_questions':len(Question.query.all())
            })
        except:
            abort(422)

    @app.route('/categories/<int:category_id>/questions')
    def access_questions_by_category(category_id):
        selection = Question.query.filter(Question.category == category_id).all()
        current_questions = paginate_questions(request, selection)
        category = Category.query.get(category_id)
        # check if range exceeded
        if len(current_questions) == 0:
            abort(404)
        return jsonify(
            {
                "questions": current_questions,
                "total_questions": len(selection),
                "current_category": category.type,
            }
        )

    @app.route('/quizzes', methods=['POST'])
    def get_quiz():
        try:
            body = request.get_json()
            category = body.get('quiz_category', None)
            previous_questions = body.get('previous_questions', None)
            if category == None or previous_questions == None:
                abort(422)
            if category['type'] == 'click' and category['id'] == 0:
                questions = Question.query.filter(Question.id.notin_((previous_questions))).all()
            else:
                category_id = category['id']
                questions = Question.query.filter_by(category=category_id).filter(Question.id.notin_((previous_questions))).all()
            if not len(questions):
                response = None
            else:
                option = random.randrange(0, len(questions))
                feedback = questions[option].format()
        
            return jsonify({
                'success': True,
                'question': feedback
            })
        except Exception as e:
            abort(422)
        

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        print(error)
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
        "success": False, 
        "error": 400, 
        "message": "bad request"}), 400
    return app

