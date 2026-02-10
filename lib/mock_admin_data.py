"""Mock admin dashboard data"""

dashboard_stats = [
    {
        'label': 'Total Photos',
        'value': '1,234',
        'icon': 'folder',
        'color': 'blue'
    },
    {
        'label': 'Active Galleries',
        'value': '28',
        'icon': 'folder',
        'color': 'green'
    },
    {
        'label': 'Client Projects',
        'value': '12',
        'icon': 'users',
        'color': 'purple'
    },
    {
        'label': 'This Month Views',
        'value': '45,678',
        'icon': 'bar-chart',
        'color': 'orange'
    }
]

recent_galleries = [
    {
        'id': 1,
        'name': 'Wedding - Sarah & John',
        'type': 'Client Review',
        'photos': 156,
        'views': 234,
        'status': 'Active',
        'lastUpdated': '2 hours ago'
    },
    {
        'id': 2,
        'name': 'Corporate Headshots',
        'type': 'Public',
        'photos': 89,
        'views': 1234,
        'status': 'Published',
        'lastUpdated': '1 day ago'
    },
    {
        'id': 3,
        'name': 'Nature Portfolio',
        'type': 'Portfolio',
        'photos': 234,
        'views': 5678,
        'status': 'Published',
        'lastUpdated': '3 days ago'
    },
    {
        'id': 4,
        'name': 'Street Photography',
        'type': 'Draft',
        'photos': 67,
        'views': 0,
        'status': 'Draft',
        'lastUpdated': '1 week ago'
    }
]
