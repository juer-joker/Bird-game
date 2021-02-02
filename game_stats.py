class GameStats:
    """跟踪游戏统计信息"""

    def __init__(self, sets):
        """初始化"""
        self.sets = sets
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """初始化运行期间可能变化的统计信息"""
        self.bird_left = self.sets.bird_limit
