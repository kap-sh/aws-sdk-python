"""Generated from Smithy shape ``com.amazonaws.wickr#Bots``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wickr.types.bot

Bots: TypeAlias = list["capo_wickr.types.bot.Bot"]


# --- restJson1 ser/de ---
def serialize_json(value: Bots) -> list:
    import capo_wickr.types.bot

    out: list = []
    for item in value:
        out.append(capo_wickr.types.bot.serialize_json(item))
    return out


def deserialize_json(data: list) -> Bots:
    import capo_wickr.types.bot

    out: Bots = []
    for item in data:
        out.append(capo_wickr.types.bot.deserialize_json(item))
    return out
