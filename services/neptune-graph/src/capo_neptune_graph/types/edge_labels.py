"""Generated from Smithy shape ``com.amazonaws.neptunegraph#EdgeLabels``."""

from typing import TypeAlias

EdgeLabels: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: EdgeLabels) -> list:
    return list(value)


def deserialize_json(data: list) -> EdgeLabels:
    return list(data)
