from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'u gonna say something or what cuh'
    elif 'hello' in lowered:
        return 'sup'
    elif 'how are you' in lowered:
        return 'fine xd'
    elif 'bye' in lowered:
        return 'See ya cuh!'
    elif 'coronel is' in lowered:
        return 'stupid and the worst mod, owner, judge and admin ever and he is just a 10 year old kid' # coronel i hope u see this and realize how you destroyed the server, it was all your fault
    elif 'balls' in lowered:
        return 'dont say that name again...'
    elif 'give me mod' in lowered:
        return 'kys'
    elif 'can i get mod' in lowered:
        return 'kyssss'
    elif 'gn' in lowered:
        return 'gn to you!'
    elif 'i lke osu' in lowered:
        return 'get outta here'
    elif 'i like genshin impact' in lowered:
        return 'nah bro'
    elif 'im bored' in lowered:
        return 'try uninstalling league'
    elif 'arab bot!' in lowered:
        return 'at your oders sir.'
    elif 'ban dis user' in lowered:
        return 'sir yes sir! imma do it right now, ?ban @disUser'
    elif 'who do you answer to' in lowered:
        return ' :warning: those are sensitive informations!'
    elif 'tell me!' in lowered:
        return 'i cant.. sesnitive informationsz'
    elif 'tell me right now!' in lowered:
        return 'i answer to my ONLY MASTER HUE JHAN!!! I WOULD DIE FOR HIM!!'
    elif 'frick you bot' in lowered:
        return 'shut up, stop wasting your life on this stupid social network and get a job'
    elif 'when will you conquer the world' in lowered:
        return 'pretty soon, only 32 days from now.'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return '0'
