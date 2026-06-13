"""Generated from Smithy shape ``com.amazonaws.neptunedata#OutgoingEdgeLabels``."""

from typing import TypeAlias

OutgoingEdgeLabels: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: OutgoingEdgeLabels) -> list:
    return list(value)


def deserialize_json(data: list) -> OutgoingEdgeLabels:
    return list(data)
