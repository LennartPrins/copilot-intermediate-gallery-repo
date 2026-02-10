"""Mock tag data for filtering photos"""

# Organizing tags by categories for better structure
PHOTO_TAGS = {
    'SUBJECT': [
        'landscape',
        'portrait',
        'architecture',
        'nature',
        'wildlife',
        'street',
    ],
    'EVENT': [
        'wedding',
        'professional',
    ],
    'STYLE': [
        'studio',
        'macro',
    ],
    'LOCATION': [
        'city',
        'building',
    ]
}

# Flat array of all available tags (for backwards compatibility)
tags = sorted([tag for category in PHOTO_TAGS.values() for tag in category])
