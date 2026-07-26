"""Generated from Smithy shape ``com.amazonaws.neptunedata#NodeLabels``."""

from typing import TypeAlias

NodeLabels: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: NodeLabels) -> list:
    return list(value)


def deserialize_json(data: list) -> NodeLabels:
    return list(data)
