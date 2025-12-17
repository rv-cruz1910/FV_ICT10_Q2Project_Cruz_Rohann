from pyscript import display, document

# Dictionary containing information about school clubs
clubs = {
    "socsci": {
        "name": "Social Science Club",
        "description": "Explore social sciences through discussions and activities.",
        "meeting_time": "Tuesday 03:00 - 4:00 PM",
        "location": "Room 409",
        "club_moderator": "Mr. Jeremy Lim",
        "members": "20"
    },

    "science": {
        "name": "Science Club",
        "description": "Conduct experiments and explore scientific concepts.",
        "meeting_time": "Tuesday 03:00 - 04:00 PM",
        "location": "Room 404",
        "club_moderator": "Ms. Jameelyn Maramag",
        "members": "20"
    },

    "cac": {
        "name": "Communication and Arts Club",
        "description": "Develop creativity through communication and artistic activities.",
        "meeting_time": "Wed 03:00–04:00 PM, Fri 03:00–04:00 PM",
        "location": "Room 406",
        "club_moderator": "Ms. Yannis Fernandez",
        "members": "20"
    },

    "glee": {
        "name": "Glee Club",
        "description": "Sing, perform, and develop vocal and musical talents.",
        "meeting_time": "Monday 03:00–05:00 PM",
        "location": "High School Music Room",
        "club_moderator": "Mr. Denver Martin",
        "members": "20"
    },

    "band": {
        "name": "Band",
        "description": "Join the school band and enhance instrumental performance skills.",
        "meeting_time": "Tue & Wed 03:00–4:30 PM",
        "location": "Band Room",
        "club_moderator": "Mr. Emilio Alumno",
        "members": "20"
    },

    "cocc": {
        "name": "Citizen Army Training Officers Club (COCC)",
        "description": "Train discipline and leadership through military-style activities.",
        "meeting_time": "Wednesday 02:30–04:30 PM",
        "location": "Quadrangle / Teatro Preciosa",
        "club_moderator": "SSgt. Jemima David PA (Res)",
        "members": "20"
    },

    "bb": {
        "name": "Basketball Club",
        "description": "Improve basketball skills through training and practice games.",
        "meeting_time": "Monday 03:00–04:00 PM",
        "location": "Quadrangle",
        "club_moderator": "Mr. Adrian Ruiz",
        "members": "20"
    },

    "vb": {
        "name": "Volleyball Club",
        "description": "Learn and practice volleyball skills and team coordination.",
        "meeting_time": "Wednesday 03:00–04:00 PM",
        "location": "Quadrangle",
        "club_moderator": "Mr. Adrian Ruiz",
        "members": "20"
    }
}


# Function to display club information based on user selection
def load_club(e):
    # Get the selected club value from dropdown
    select = document.getElementById("clubSelect")
    club_id = select.value

    # Get club information or default values if not found
    club = clubs.get(club_id, {
        "name": "Not found",
        "description": "Not found",
        "meeting_time": "Not found",
        "location": "Not found",
        "club_moderator": "Not found",
        "members": "Not found"
    })

    # Format the output text
    output_text = f"""
    Club Name: {club.get('name', 'Not found')}
    Description: {club.get('description', 'Not found')}
    Meeting Time: {club.get('meeting_time', 'Not found')}
    Location: {club.get('location', 'Not found')}
    Club Moderator: {club.get('club_moderator', 'Not found')}
    Number of Members: {club.get('members', 'Not found')}
    """

    # Display the formatted text in the output element
    display(output_text, target="output")
