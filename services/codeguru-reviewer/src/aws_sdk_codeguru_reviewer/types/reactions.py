"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#Reactions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.reaction

Reactions: TypeAlias = list["aws_sdk_codeguru_reviewer.types.reaction.Reaction"]


# --- restJson1 ser/de ---
def serialize_json(value: Reactions) -> list:
    import aws_sdk_codeguru_reviewer.types.reaction

    out: list = []
    for item in value:
        out.append(aws_sdk_codeguru_reviewer.types.reaction.serialize_json(item))
    return out


def deserialize_json(data: list) -> Reactions:
    import aws_sdk_codeguru_reviewer.types.reaction

    out: Reactions = []
    for item in data:
        out.append(aws_sdk_codeguru_reviewer.types.reaction.deserialize_json(item))
    return out
