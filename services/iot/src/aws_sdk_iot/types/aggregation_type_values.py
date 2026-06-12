"""Generated from Smithy shape ``com.amazonaws.iot#AggregationTypeValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.aggregation_type_value

AggregationTypeValues: TypeAlias = list[
    "aws_sdk_iot.types.aggregation_type_value.AggregationTypeValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregationTypeValues) -> list:
    return list(value)


def deserialize_json(data: list) -> AggregationTypeValues:
    return list(data)
