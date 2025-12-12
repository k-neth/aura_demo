"""
AURA Backend API Server
Serves mock data and static files
"""
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import json
import random
from datetime import datetime, timedelta
from pathlib import Path
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)  # Enable Cross-Origin Requests

# Sample data for Kenya
KENYA_COUNTIES = [
    'Nairobi', 'Mombasa', 'Kisumu', 'Nakuru', 'Eldoret', 'Thika', 'Malindi',
    'Kitale', 'Garissa', 'Kakamega', 'Bungoma', 'Meru', 'Nyeri', 'Machakos',
    'Kisii', 'Kericho', 'Uasin Gishu', 'Kiambu', 'Kilifi', 'Muranga'
]

def generate_dashboard_stats():
    """Generate dashboard statistics"""
    return {
        'digital_inclusion_rate': 68.4,
        'transactions_analyzed': '1.2B',
        'active_policies': 148,
        'smes_tracked': '2.1M',
        'monthly_growth': '+2.3%',
        'fraud_detection_rate': 94.5
    }

def generate_regions():
    """Generate region data for heatmap"""
    regions = [
        {
            'id': 1,
            'name': 'Nairobi',
            'inclusion_rate': 85,
            'x': 45, 'y': 35,
            'width': 8, 'height': 6,
            'barrier': 'Digital Literacy',
            'top_service': 'M-PESA Lipa Na',
            'population': '4.4M',
            'recommendation': 'Implement digital literacy programs targeting youth in informal settlements'
        },
        {
            'id': 2,
            'name': 'Mombasa',
            'inclusion_rate': 65,
            'x': 60, 'y': 60,
            'width': 7, 'height': 5,
            'barrier': 'Agent Availability',
            'top_service': 'Airtel Money',
            'population': '1.2M',
            'recommendation': 'Increase agent banking network by 30% in underserved areas'
        },
        {
            'id': 3,
            'name': 'Western',
            'inclusion_rate': 45,
            'x': 30, 'y': 50,
            'width': 12, 'height': 9,
            'barrier': 'Network Coverage',
            'top_service': 'T-Kash',
            'population': '2.3M',
            'recommendation': 'Partner with telecom providers to expand 4G coverage in rural areas'
        },
        {
            'id': 4,
            'name': 'Northeastern',
            'inclusion_rate': 32,
            'x': 65, 'y': 20,
            'width': 15, 'height': 11,
            'barrier': 'Infrastructure',
            'top_service': 'Bank Transfers',
            'population': '1.8M',
            'recommendation': 'Deploy mobile banking vans and satellite internet solutions'
        }
    ]
    return regions

def generate_alerts():
    """Generate system alerts"""
    return [
        {
            'id': 1,
            'title': 'Youth Digital Credit Overuse Detected',
            'description': '18-25 age group showing 40% increase in digital loan defaults',
            'region': 'Nairobi & Mombasa',
            'population': '450,000 affected',
            'priority': 'high'
        },
        {
            'id': 2,
            'title': 'Rural Women Digital Savings Gap',
            'description': 'Only 28% of rural women in Western Kenya using digital savings',
            'region': 'Western Region',
            'population': '1.2M affected',
            'priority': 'medium'
        }
    ]

def generate_sme_data():
    """Generate SME data"""
    return {
        'total_smes': 2100000,
        'digital_adoption': 64,
        'at_risk_smes': 12.4,
        'avg_revenue': 245000,
        'sectors': [
            {'name': 'Retail & Trade', 'growth': 22, 'revenue': 185000, 'risk': 'Low'},
            {'name': 'Agriculture', 'growth': 8, 'revenue': 125000, 'risk': 'Medium'},
            {'name': 'Transport', 'growth': 35, 'revenue': 245000, 'risk': 'Low'},
            {'name': 'Manufacturing', 'growth': -5, 'revenue': 310000, 'risk': 'High'}
        ]
    }

def generate_monthly_data():
    """Generate monthly transaction data"""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    return {
        'labels': months,
        'datasets': [
            {
                'label': 'M-PESA',
                'data': [120, 135, 142, 155, 168, 175, 182, 190, 205, 218, 225, 240],
                'color': '#4CAF50'
            },
            {
                'label': 'Bank Apps',
                'data': [45, 48, 52, 55, 58, 62, 65, 68, 72, 75, 78, 82],
                'color': '#2196F3'
            },
            {
                'label': 'FinTech',
                'data': [18, 22, 25, 28, 32, 35, 38, 42, 45, 48, 52, 55],
                'color': '#9C27B0'
            }
        ]
    }

# API Routes
@app.route('/')
def serve_index():
    """Serve the main dashboard"""
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Serve static files"""
    return send_from_directory(app.static_folder, path)

@app.route('/api/dashboard/stats')
def api_dashboard_stats():
    """Get dashboard statistics"""
    return jsonify(generate_dashboard_stats())

@app.route('/api/regions')
def api_regions():
    """Get region data for heatmap"""
    return jsonify(generate_regions())

@app.route('/api/alerts')
def api_alerts():
    """Get system alerts"""
    return jsonify(generate_alerts())

@app.route('/api/sme')
def api_sme():
    """Get SME data"""
    return jsonify(generate_sme_data())

@app.route('/api/transactions/monthly')
def api_monthly_transactions():
    """Get monthly transaction data"""
    return jsonify(generate_monthly_data())

@app.route('/api/policy/simulate', methods=['POST'])
def api_simulate_policy():
    """Simulate policy impact"""
    # For demo, return mock simulation results
    import random
    results = {
        'inclusion_change': round(random.uniform(2.0, 8.0), 1),
        'transaction_volume': round(random.uniform(10, 25), 0),
        'sme_benefit': round(random.uniform(5, 15), 0),
        'revenue_impact': round(random.uniform(-3.0, 1.0), 1),
        'recommendation': 'Based on historical data, this policy change is projected to increase digital inclusion by 4.2%. Recommend gradual implementation over 6 months.'
    }
    return jsonify(results)

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    print("""
    🌟 AURA Demo Server Starting...
    
    📊 Dashboard:     http://localhost:5000
    🗺️  Heatmap:      http://localhost:5000/heatmap.html
    🧪 Simulator:     http://localhost:5000/simulator.html
    🏢 SME Monitor:   http://localhost:5000/sme.html
    
    🔧 API Available at:
        /api/dashboard/stats
        /api/regions
        /api/alerts
        /api/sme
        /api/transactions/monthly
    
    Press Ctrl+C to stop the server.
    """)
    
    # Create frontend directory if it doesn't exist
    frontend_dir = Path(__file__).parent.parent / 'frontend'
    frontend_dir.mkdir(exist_ok=True)
    
    app.run(host='0.0.0.0', port=5000, debug=True)