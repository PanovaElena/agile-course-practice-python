from game_of_life.model.game_of_life import GameOfLife


class GameOfLifeViewModel:
    def __init__(self):
        self.next_step_btn_state = 'disabled'
        self.remove_row_btn_state = 'disabled'
        self.remove_column_btn_state = 'disabled'

        self.rows = 2
        self.columns = 2

        self.current_color_field = []
        self.current_binary_field = []
        self.next_binary_field = []
        self.next_color_field = []

    def set_number_of_rows(self, rows):
        self.rows = rows

    def get_number_of_rows(self):
        return self.rows

    def set_number_of_columns(self, columns):
        self.columns = columns

    def get_number_of_columns(self):
        return self.columns

    def set_current_color_field(self, field):
        self.current_color_field = field

    def get_current_color_field(self):
        return self.current_color_field

    def set_next_color_field(self, field):
        self.next_color_field = field

    def get_next_color_field(self):
        return self.next_color_field

    def set_next_step_btn_state(self, state):
        self.next_step_btn_state = state

    def get_remove_row_btn_state(self, rows):
        if rows == 2:
            self.remove_row_btn_state = 'disabled'
        else:
            self.remove_row_btn_state = 'normal'
        return self.remove_row_btn_state

    def get_remove_column_btn_state(self, columns):
        if columns == 2:
            self.remove_column_btn_state = 'disabled'
        else:
            self.remove_column_btn_state = 'normal'
        return self.remove_column_btn_state

    def is_all_white(self) -> bool:
        for i in range(len(self.current_color_field)):
            for j in range(len(self.current_color_field)):
                if self.current_color_field[i][j]["bg"] == "Black":
                    return False
        return True

    def get_next_step_btn_state(self):
        if self.is_all_white():
            self.set_next_step_btn_state("disabled")
        else:
            self.set_next_step_btn_state("normal")
        return self.next_step_btn_state

    def convert_field_to_binary(self, color_field):
        self.current_binary_field.clear()
        for i in range(self.rows):
            self.current_binary_field.append([])
            for j in range(self.columns):
                if color_field[i][j]["bg"] == "Black":
                    self.current_binary_field[i].append(1)
                else:
                    self.current_binary_field[i].append(0)

    def convert_field_to_color(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.next_binary_field[i][j] == 1:
                    self.next_color_field[i][j]['bg'] = "Black"
                else:
                    self.next_color_field[i][j]['bg'] = "White"

    def compute_next_step(self):
        game = GameOfLife()
        self.convert_field_to_binary(self.current_color_field)
        self.next_binary_field = game.start(self.current_binary_field)
        self.convert_field_to_color()

    def color_changed(self, i, j):
        if self.current_color_field[i][j]["bg"] == "White":
            self.current_color_field[i][j]["bg"] = "Black"
        else:
            self.current_color_field[i][j]["bg"] = "White"

    def clicked_remove(self, new):
        if new == 'row' and self.rows > 2:
            self.rows -= 1
        if new == 'column' and self.columns > 2:
            self.columns -= 1

    def clicked_add(self, new):
        if new == 'row':
            self.rows += 1
        if new == 'column':
            self.columns += 1
