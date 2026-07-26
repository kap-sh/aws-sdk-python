"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#Reactions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.reaction

Reactions: TypeAlias = list["capo_codeguru_reviewer.types.reaction.Reaction"]


# --- restJson1 ser/de ---
def serialize_json(value: Reactions) -> list:
    import capo_codeguru_reviewer.types.reaction

    out: list = []
    for item in value:
        out.append(capo_codeguru_reviewer.types.reaction.serialize_json(item))
    return out


def deserialize_json(data: list) -> Reactions:
    import capo_codeguru_reviewer.types.reaction

    out: Reactions = []
    for item in data:
        out.append(capo_codeguru_reviewer.types.reaction.deserialize_json(item))
    return out
