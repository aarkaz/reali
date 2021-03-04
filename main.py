import database
import controller

if __name__ == '__main__':
    database.initialize()
    controller.app.run(debug=True)