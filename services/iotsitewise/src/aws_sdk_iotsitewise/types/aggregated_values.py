"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AggregatedValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.aggregated_value

AggregatedValues: TypeAlias = list[
    "aws_sdk_iotsitewise.types.aggregated_value.AggregatedValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregatedValues) -> list:
    import aws_sdk_iotsitewise.types.aggregated_value

    out: list = []
    for item in value:
        out.append(aws_sdk_iotsitewise.types.aggregated_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> AggregatedValues:
    import aws_sdk_iotsitewise.types.aggregated_value

    out: AggregatedValues = []
    for item in data:
        out.append(aws_sdk_iotsitewise.types.aggregated_value.deserialize_json(item))
    return out
