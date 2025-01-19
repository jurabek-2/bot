from aiogram.dispatcher.filters.state import State,StatesGroup



class ReklmaState(StatesGroup):
    rek=State()




class AddKino(StatesGroup):
    media=State
    media_id=State()


class AddChannelsState(StatesGroup):
    username=State
    channell_id=State()


class DleteChannelState(StatesGroup):
    username=State()


class DeleteMovieState(StatesGroup):
    post_id=State()
