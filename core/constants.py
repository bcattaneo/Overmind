
class WorkerStatuses:
    OFF = 'off'
    IDLE = 'idle'
    BUSY = 'busy'

WORKER_STATUSES = [WorkerStatuses.IDLE, WorkerStatuses.BUSY, WorkerStatuses.OFF]
WORKER_STATUS_CHOICES = [(x.capitalize(), x) for x in WORKER_STATUSES]


class TaskStatuses:
    NEW = 'new'
    WAITING = 'waiting'
    DONE = 'done'

TASK_STATUSES = [TaskStatuses.NEW, TaskStatuses.WAITING, TaskStatuses.DONE]
TASK_STATUS_CHOICES = [(x.capitalize(), x) for x in TASK_STATUSES]


class Races:
    PROTOS = 'protos'
    ZERG = 'zerg'
    TERRAN = 'terran'

RACES = [Races.PROTOS, Races.ZERG, Races.TERRAN]
RACE_CHOICES = [(x.capitalize(), x) for x in RACES]


class PlayerType:
    HUMAN = 'human'
    RANDOM_BOT = 'random'
    CBL_BOT_1 = 'cbl_1'
    COMPUTER_EASY = 'easy'
    COMPUTER_MEDIUM = 'medium'
    COMPUTER_HARD = 'hard'

PLAYER_TYPES = [PlayerType.HUMAN,
                PlayerType.RANDOM_BOT,
                PlayerType.CBL_BOT_1,
                PlayerType.COMPUTER_EASY,
                PlayerType.COMPUTER_MEDIUM,
                PlayerType.COMPUTER_HARD]
PLAYER_TYPE_CHOICES = [(x.capitalize(), x) for x in PLAYER_TYPES]