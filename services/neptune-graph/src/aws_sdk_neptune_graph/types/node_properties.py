"""Generated from Smithy shape ``com.amazonaws.neptunegraph#NodeProperties``."""

from typing import TypeAlias

NodeProperties: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: NodeProperties) -> list:
    return list(value)


def deserialize_json(data: list) -> NodeProperties:
    return list(data)
