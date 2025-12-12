"""
Simple mock data generator for AURA
"""
import json
import random
from datetime import datetime

def generate_mock_transactions(count=100):
    """Generate mock transaction data"""
    transactions = []
    for i in range(count):
        transactions.append({
            'id': i,
            'amount': random.randint(100, 50000),
            'channel': random.choice(['M-PESA', 'Airtel Money', 'Bank Transfer']),
            'region': random.choice(['Nairobi', 'Mombasa', 'Western', 'Central']),
            'timestamp': datetime.now().isoformat()
        })
    return transactions

def save_sample_data():
    """Save sample data to JSON files"""
    data = {
        'dashboard_stats': {
            'digital_inclusion_rate': 68.4,
            'transactions_analyzed': '1.2B',
            'active_policies': 148,
            'smes_tracked': '2.1M'
        }
    }
    
    with open('sample_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print("Sample data saved to sample_data.json")
    return data

if __name__ == '__main__':
    save_sample_data()
    