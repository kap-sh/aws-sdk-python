"""Generated from Smithy shape ``com.amazonaws.wellarchitected#Choices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.choice

Choices: TypeAlias = list["aws_sdk_wellarchitected.types.choice.Choice"]


# --- restJson1 ser/de ---
def serialize_json(value: Choices) -> list:
    import aws_sdk_wellarchitected.types.choice

    out: list = []
    for item in value:
        out.append(aws_sdk_wellarchitected.types.choice.serialize_json(item))
    return out


def deserialize_json(data: list) -> Choices:
    import aws_sdk_wellarchitected.types.choice

    out: Choices = []
    for item in data:
        out.append(aws_sdk_wellarchitected.types.choice.deserialize_json(item))
    return out
