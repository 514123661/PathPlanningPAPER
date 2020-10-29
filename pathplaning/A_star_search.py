import heapq

class Map:
    def __init__(self,size = (548,421)):
        x,y = size
        self.x = x
        self.y = y
        self.wall = []

    def is_bound(self, point):
        x, y = point

        return 1 < x < self.x and 1 < y < self.y

    def is_able(self, point):
        return point not in self.wall

    def neib(self, current):

        x, y = current
        ans = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        ans = list(filter(self.is_bound, ans))
        ans = list(filter(self.is_able, ans))
        return ans

class Priorityqueue:
    def __init__(self):
        self.element = []

    def empty(self):
        return len(self.element) == 0

    def put(self, point, priority):

        heapq.heappush(self.element, (priority, point))

    def get(self):
        return heapq.heappop(self.element)[1]


def heruistic(a,b):
    ax, ay = a
    bx, by = b
    return abs(ax-bx) + abs(ay-by)

def A_Star(Map, Start, End):

    print('searching....')

    frontier = Priorityqueue()

    frontier.put(Start, 0)

    came_from = {}

    cost_so_far = {}

    came_from[Start] = None

    cost_so_far[Start] = 0

    while not frontier.empty():

        current = frontier.get()
        if current == End:
            print('get a path!')
            break

        for next in Map.neib(current=current):

            new_cost = cost_so_far[current]+ 2 #2 is a set value.it can be changed.

            if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost

                    pripority_ = new_cost + heruistic(current,next)

                    frontier.put(next, pripority_)

                    came_from[next] = current

    else:
        print('cannot find a path!!')
        return 'fuck','fuck'
    return came_from, cost_so_far










