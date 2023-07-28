from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Cookie_order:
    DB = "cookie_orders"
    def __init__(self,data):
        #Keep the same as database!
        self.id = data["id"]
        self.name = data["name"]
        self.cookie_type = data["cookie_type"]
        self.num_boxes = data["num_boxes"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_one(cls, order_id):
        query = """
                SELECT * from cookie_orders
                WHERE id = %(id)s
                """
        order_dictionary = connectToMySQL(cls.DB).query_db(query, {"id": order_id})
        order = Cookie_order(order_dictionary[0])

        return order
 



    @classmethod
    def get_all(cls):
        all_orders_list = []

        query = "SELECT * from cookie_orders"
        all_orders_data = connectToMySQL(cls.DB).query_db(query)

        for order in all_orders_data:
            new_order_object = Cookie_order(order)
            all_orders_list.append(new_order_object)
        return all_orders_list


    @classmethod
    def save(cls, data):
        query = """
                INSERT into cookie_orders (name, cookie_type, num_boxes) 
                VALUES (%(name)s, %(cookie_type)s, %(num_boxes)s);
                """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result

    @classmethod
    def edit(cls, data):
        query = """
                UPDATE cookie_orders
                SET name = %(name)s,cookie_type = %(cookie_type)s, num_boxes = %(num_boxes)s
                WHERE id = %(id)s;
                """ 
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

    @staticmethod
    def validate_cookie_order(data):
        is_valid = True
        # check if each field is blank
        if len(data["name"]) == 0:
            flash("Name required.")
            is_valid = False
        if len(data["cookie_type"]) == 0:
            flash("Cookie Type required.")
            is_valid = False
        if len(data["num_boxes"]) == 0:
            flash("Number of Boxes required.")
            is_valid = False
        elif int(data["num_boxes"]) <= 0:
            flash("Number of boxes must be a positive number.")
            is_valid = False
        # check if number of cookies is positive
        elif len(data["name"]) <=2:
            flash("Must be at least 2 characters.")
            is_valid = False
        elif len(data["cookie_type"]) <=2:
            flash("Must be at least 2 characters.")
            is_valid = False
        return is_valid