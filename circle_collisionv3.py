width, height = 600, 600

def setup():
    size(width, height)
    background(0)
    
segment1 = {'x1':50, 'y1':200, 'x2':width-200, 'y2':height-100}
segment2 = {'x1':200, 'y1':400, 'x2':width-100, 'y2':height-450}

circle1 = {'x':300, 'y':200, 'r':width/12, 'vector':PVector(-0.5, 0.5, 0)}
circle2 = {'x':100, 'y':200, 'r':width/12, 'vector':PVector(-0.5, 0.5, 0)}

circles = [circle1, circle2]
segments = [segment1, segment2]
def draw():
    if mousePressed:
        frameRate(5)
    else:
        frameRate(100)
    background(0)
    strokeWeight(3)
        
    # ---segments
    stroke(0, 235, 255)
    for lines in segments:
        line(lines['x1'], lines['y1'], lines['x2'], lines['y2'])
        
    for each in circles:
    
        # ---circle1
        fill(0, 235, 255)
        circle(each['x'], each['y'], each['r'])
        
        # ---Velocity vector
        stroke(255, 0, 0)
        counter2 = 25
        line(each['x'], each['y'], each['x'] + each['vector'].x*counter2, each['y'] + each['vector'].y*counter2) 
        
        for lines in segments:
            # ---finds distance between circle 1 and closest point on segment
            a = dist(lines['x1'], lines['y1'], lines['x2'], lines['y2'])
            b = dist(lines['x1'], lines['y1'], each['x'], each['y'])
            c = dist(lines['x2'], lines['y2'], each['x'], each['y'])
            p = (a + b + c)/2
            area = sqrt(p * (p - a) * (p - b) * (p - c))    
            distance = 2 * (area/a)
            
            # # ---circle from each center with radius of distance
            # noFill()
            # stroke(255, 0, 0)
            # circle(each['x'], each['y'], distance * 2)
                
            if floor(distance) <= each['r']/2 and lines['x1'] < each['x'] < lines['x2']:
                # ---normalized perpendicular vector to segment1
                d = PVector(each['vector'].x, each['vector'].y)
                n = PVector(lines['x2'] - lines['x1'], lines['y2'] - lines['y1']).normalize()
                r = d - (2 * d.dot(n)) * n
                r *= -1
                each['vector'] = r
        
        # ---velocity
        each['x'] += each['vector'].x
        each['y'] += each['vector'].y
        # ---gravity
        each['vector'].y += 0.05
        
        
        
    
    
