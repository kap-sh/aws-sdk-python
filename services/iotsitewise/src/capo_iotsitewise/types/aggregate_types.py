"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AggregateTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.aggregate_type

AggregateTypes: TypeAlias = list["capo_iotsitewise.types.aggregate_type.AggregateType"]


# --- restJson1 ser/de ---
def serialize_json(value: AggregateTypes) -> list:
    import capo_iotsitewise.types.aggregate_type

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.aggregate_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> AggregateTypes:
    import capo_iotsitewise.types.aggregate_type

    out: AggregateTypes = []
    for item in data:
        out.append(capo_iotsitewise.types.aggregate_type.deserialize_json(item))
    return out
