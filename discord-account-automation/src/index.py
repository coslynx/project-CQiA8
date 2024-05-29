import automation.form_filling
import automation.email_verification
import automation.proxy_support
import data_generation.random_data
import error_handling.error_handling
import logging.logging
import enhancements.captcha_solving
import enhancements.multi_threading
import enhancements.account_verification
import enhancements.user_agent_rotation
import enhancements.gui_interface

if __name__ == "__main__":
    # Main entry point of the Discord account automation script
    automation.form_filling.fill_form()
    automation.email_verification.verify_email()
    automation.proxy_support.use_proxy()
    data_generation.random_data.generate_data()
    error_handling.error_handling.handle_errors()
    logging.logging.log_actions()
    enhancements.captcha_solving.solve_captcha()
    enhancements.multi_threading.run_multi_threading()
    enhancements.account_verification.verify_account()
    enhancements.user_agent_rotation.rotate_user_agent()
    enhancements.gui_interface.create_gui_interface()