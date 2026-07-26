"""Generated from Smithy shape ``com.amazonaws.groundstation#DataflowEdge``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.config_arn

DataflowEdge: TypeAlias = list["capo_groundstation.types.config_arn.ConfigArn"]


# --- restJson1 ser/de ---
def serialize_json(value: DataflowEdge) -> list:
    return list(value)


def deserialize_json(data: list) -> DataflowEdge:
    return list(data)
