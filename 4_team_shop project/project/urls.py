import main_page
import registration_page
from .settings import shop

main_page.main.add_url_rule(rule = "/", view_func= main_page.render_main)
registration_page.registration.add_url_rule(rule = "/registration/", view_func= registration_page.render_registration, methods = ["GET", "POST"])

shop.register_blueprint(blueprint= main_page.main)
shop.register_blueprint(blueprint= registration_page.registration)