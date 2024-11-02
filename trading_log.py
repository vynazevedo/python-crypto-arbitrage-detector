import csv
import datetime
import os

def log_trade(filename, asset1, asset2, asset3, invest, return_, fee, profit, net_profit):
    fieldnames = ['time', 'asset1', 'asset2', 'asset3', 'invest', 'return', 'fee', 'profit', 'net_profit']
    trade_data = {
        'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'asset1': asset1,
        'asset2': asset2,
        'asset3': asset3,
        'invest': invest,
        'return': return_,
        'fee': fee,
        'profit': profit,
        'net_profit': net_profit
    }
    
    write_header = not os.path.exists(filename)
    with open(filename, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow(trade_data)

def compile_summary(filename):
    total_profit = 0
    total_trades = 0
    total_invested = 0
    
    with open(filename, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_profit += float(row['net_profit'])
            total_trades += 1
            total_invested += float(row['invest'])

    return {
        'total_profit': total_profit,
        'total_number_of_trades': total_trades,
        'total_invested': total_invested,
        'average_profit_per_trade': total_profit / total_trades if total_trades > 0 else 0
    }
