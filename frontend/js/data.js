// Mock data for AURA demo
const AURA_DATA = {
    // Dashboard stats
    stats: {
        inclusionRate: 68.4,
        transactions: '1.2B',
        policies: 148,
        smes: '2.1M'
    },
    
    // Regions for heatmap
    regions: [
        {
            id: 1,
            name: 'Nairobi',
            inclusion: 85,
            x: 45, y: 35,
            barrier: 'Digital Literacy',
            recommendation: 'Digital literacy programs for youth'
        },
        {
            id: 2,
            name: 'Mombasa',
            inclusion: 65,
            x: 60, y: 60,
            barrier: 'Agent Availability',
            recommendation: 'Increase agent network by 30%'
        }
    ],
    
    // SME sectors
    sectors: [
        { name: 'Retail', growth: 22, risk: 'Low' },
        { name: 'Agriculture', growth: 8, risk: 'Medium' },
        { name: 'Transport', growth: 35, risk: 'Low' },
        { name: 'Manufacturing', growth: -5, risk: 'High' }
    ],
    
    // Generate random transaction
    generateTransaction: function() {
        const channels = ['M-PESA', 'Airtel Money', 'Bank Transfer'];
        const regions = ['Nairobi', 'Mombasa', 'Western', 'Central'];
        
        return {
            id: Date.now(),
            amount: Math.floor(Math.random() * 50000) + 100,
            channel: channels[Math.floor(Math.random() * channels.length)],
            region: regions[Math.floor(Math.random() * regions.length)],
            timestamp: new Date().toISOString()
        };
    }
};

// Export for browser
if (typeof window !== 'undefined') {
    window.AURA_DATA = AURA_DATA;
}