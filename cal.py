import math

def cal(initial_value,profit_margin,end_margin,turn_over,process):
    amount = [0,0]
    final = []
    if process == 'normal':
        values = [100/96*(profit_margin+initial_value)]
        profit = [values[-1]*96/100-initial_value]
        for i in range(turn_over-2):
            val = (100/96*(profit_margin+sum(values)+initial_value*(1-0.96*len(values))))
            profit.append(val*96/100-sum(values)-initial_value*(1-0.96*len(values)))
            values.append(val)
        loss = sum(values) - 0.96*initial_value*len(values) + (7-len(values))*initial_value
        for i in values:
            final.append([initial_value,i])
        final.append([17.21*(loss+end_margin),18.97*(loss+end_margin)])
    elif process == 'round':
        values = [int(round(100/96*(profit_margin+initial_value)))]
        profit = [values[-1]*96/100-initial_value]
        for i in range(turn_over-2):
            val = int(round(100/96*(profit_margin+sum(values)+initial_value*(1-0.96*len(values)))))
            profit.append(val*96/100-sum(values)-initial_value*(1-0.96*len(values)))
            values.append(val)
        loss = sum(values) - 0.96*initial_value*len(values) + (7-len(values))*initial_value
        for i in values:
            final.append([initial_value,i])
        final.append([int(round(17.21*(loss+end_margin))),int(round(18.97*(loss+end_margin)))])
    elif process == 'slow':
        values = [int(math.floor(100/96*(profit_margin+initial_value)))]
        profit = [values[-1]*96/100-initial_value]
        for i in range(turn_over-2):
            val = int(math.floor(100/96*(profit_margin+sum(values)+initial_value*(1-0.96*len(values)))))
            profit.append(val*96/100-sum(values)-initial_value*(1-0.96*len(values)))
            values.append(val)
        loss = sum(values) - 0.96*initial_value*len(values) + (7-len(values))*initial_value
        for i in values:
            final.append([initial_value,i])
        final.append([int(math.floor(17.21*(loss+end_margin))),int(math.floor(18.97*(loss+end_margin)))])
    else:
        values = [int(math.ceil(100/96*(profit_margin+initial_value)))]
        profit = [values[-1]*96/100-initial_value]
        for i in range(turn_over-2):
            val = int(math.ceil(100/96*(profit_margin+sum(values)+initial_value*(1-0.96*len(values)))))
            profit.append(val*96/100-sum(values)-initial_value*(1-0.96*len(values)))
            values.append(val)
        loss = sum(values) - 0.96*initial_value*len(values) + (7-len(values))*initial_value
        for i in values:
            final.append([initial_value,i])
        final.append([int(math.ceil(17.21*(loss+end_margin))),int(math.ceil(18.97*(loss+end_margin)))])
    profit.append([final[-1][0]*2.16-loss-sum(final[-1]),final[-1][1]*1.96-loss-sum(final[-1])])
    for k in final:
        amount[0] += k[0]
        amount[1] += k[1]
    amount.append(sum(amount))
    
    return str(final) + '\n\n' + str(profit) + '\n\n' + str(amount)