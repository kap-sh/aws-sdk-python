"""Generated from Smithy shape ``com.amazonaws.guardduty#IndicatorValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.indicator_value_string

IndicatorValues: TypeAlias = list[
    "aws_sdk_guardduty.types.indicator_value_string.IndicatorValueString"
]


# --- restJson1 ser/de ---
def serialize_json(value: IndicatorValues) -> list:
    return list(value)


def deserialize_json(data: list) -> IndicatorValues:
    return list(data)
