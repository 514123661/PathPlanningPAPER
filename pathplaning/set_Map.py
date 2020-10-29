import collections

def set_Map(current,time,date,rate):

    wall = collections.deque()

    remain_enemgy = ((60 - time)%60) / 2 -1

    hour = time//60 +3 #basetime = 3



    for x in range(1,549):
        for y in range(1,422):
            enemgy_cost = enemgy(current,(x,y))

            if enemgy_cost <= remain_enemgy:
                t = hour
            else:
                temp = enemgy_cost - remain_enemgy-1
                need_t = temp//30
                t = need_t + hour+1

            if (x,y,date,t) in rate:

                wall.append((x,y))
            
    return wall


def enemgy(current,goal):

    xc,yc = current
    xg,yg = goal

    return abs(xc-xg)+abs(yc-yg)