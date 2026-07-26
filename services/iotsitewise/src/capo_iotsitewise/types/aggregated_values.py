"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AggregatedValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.aggregated_value

AggregatedValues: TypeAlias = list[
    "capo_iotsitewise.types.aggregated_value.AggregatedValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregatedValues) -> list:
    import capo_iotsitewise.types.aggregated_value

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.aggregated_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> AggregatedValues:
    import capo_iotsitewise.types.aggregated_value

    out: AggregatedValues = []
    for item in data:
        out.append(capo_iotsitewise.types.aggregated_value.deserialize_json(item))
    return out
