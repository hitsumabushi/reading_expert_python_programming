###--
# metaclass: typeを継承している。
# これは、YieldConditionのインターフェース
# 3つのstatic methodを定めてる
###--
class MetaYieldCondition(type):

    'Metaclass for YieldCondition'

    __custom_wait_handlers = []

    def __init__(cls, cname, cbases, cdict):
        ###--
        # super(Class, self) でClassのsuperを参照している。
        # python 3からは、super().__init__(...)と書けばオッケー
        ###--
        super(MetaYieldCondition, cls).__init__(cname, cbases, cdict)

        ###--
        # for...else... 構文
        # breakした時にはelse...は実行されないのが、便利
        ###--
        for else
        for meth in ('_has_waits', '_handle_waits', '_merge'):
            if meth not in cdict:
                break
        else:
            ###--
            # __custom_wait_handlers にclsを追加しておく。
            # これは、あとで、__has_waitsなどから参照され、cls.__has_waitsなどが参照される
            ###--
            MetaYieldCondition.__custom_wait_handlers.append(cls)

    ###--
    # staticmethod デコレータ
    # selfを引数に持たない。つまり、インスタンスとはやりとりしない。
    # classmethodとの違いは、clsを暗黙的に引数に持つか持たないか。
    # 気分的には、関数をモジュールレベルじゃなくて、クラスで定義することで、オーバーライドできるようにしたもの。
    ###--
    @staticmethod
    def _has_waits(tm):
        for cls in MetaYieldCondition.__custom_wait_handlers:
            if cls._has_waits(tm):
                return True
        return False

    @staticmethod
    def _handle_waits(tm, timeout=None):
        for cls in MetaYieldCondition.__custom_wait_handlers:
            if cls._has_waits(tm):
                cls._handle_waits(tm, tm._get_run_timeout(timeout))

    @staticmethod
    def _merge(tm1, tm2):
        for cls in MetaYieldCondition.__custom_wait_handlers:
            cls._merge(tm1, tm2)

