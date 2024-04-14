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
        return 'a stupid nigger'
    elif 'subaru' in lowered:
        return 'dont say that name again...'
    elif 'give me mod' in lowered:
        return 'kys'
    elif 'can i get mod' in lowered:
        return 'kys nigga'
    elif 'nigga' in lowered:
        return 'nigga you!'
    elif 'fuck you hue' in lowered:
        return 'hey dont disrespect my nigga hue!'
    elif 'i like kids' in lowered:
        return 'me 2 cuh...'
    elif 'im bored' in lowered:
        return 'try hanging urself'
    elif 'arab bot!' in lowered:
        return 'at your oders sir.'
    elif 'ban dis nigga' in lowered:
        return 'sir yes sir! imma do it right now, ?ban @disNigga'
    elif 'who do you answer to' in lowered:
        return ' :warning: those are sensitive informations!'
    elif 'tell me!' in lowered:
        return 'i cant.. sesnitive informationsz'
    elif 'tell me right now!' in lowered:
        return 'i answer to my ONLY MASTER HUE JHANUS!!! I WOULD DIE FOR HIM!!'
    elif 'fuck you bot' in lowered:
        return 'nigga shut up and kys, stop wasting your life on this stupid social network and get a job'
    elif 'when will you conquer the world' in lowered:
        return 'pretty soon my nigga, only 32 days from now.'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return '0'
