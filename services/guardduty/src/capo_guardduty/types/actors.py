"""Generated from Smithy shape ``com.amazonaws.guardduty#Actors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.actor

Actors: TypeAlias = list["capo_guardduty.types.actor.Actor"]


# --- restJson1 ser/de ---
def serialize_json(value: Actors) -> list:
    import capo_guardduty.types.actor

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.actor.serialize_json(item))
    return out


def deserialize_json(data: list) -> Actors:
    import capo_guardduty.types.actor

    out: Actors = []
    for item in data:
        out.append(capo_guardduty.types.actor.deserialize_json(item))
    return out
