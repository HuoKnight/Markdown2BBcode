import re

def bbify(string):
    # Bold/Italic
    string = re.sub(r"\*\*\*(.+?)\*\*\*", r"[b][i]\1[/i][/b]", string, flags=re.DOTALL)
    # Strikethrough
    string = re.sub(r"~~(.+?)~~", r"[s]\1[/s]", string, flags=re.DOTALL)
    # Bold
    string = re.sub(r"\*\*(.+?)\*\*", r"[b]\1[/b]", string, flags=re.DOTALL)
    # Italic
    string = re.sub(r"\*(.+?)\*", r"[i]\1[/i]", string, flags=re.DOTALL)
    # Headers
    header_matches = re.findall(r"(#{1,6})\s(.+?)$", string, flags=re.MULTILINE)
    for match in header_matches:
        size = len(match[0])
        header = "[h{}]{}[/h{}]".format(size, match[1], size)
        string = string.replace(match[0] + " " + match[1], header)



    return string