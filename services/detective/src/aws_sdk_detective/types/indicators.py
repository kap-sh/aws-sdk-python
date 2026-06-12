"""Generated from Smithy shape ``com.amazonaws.detective#Indicators``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_detective.types.indicator

Indicators: TypeAlias = list["aws_sdk_detective.types.indicator.Indicator"]


# --- restJson1 ser/de ---
def serialize_json(value: Indicators) -> list:
    import aws_sdk_detective.types.indicator

    out: list = []
    for item in value:
        out.append(aws_sdk_detective.types.indicator.serialize_json(item))
    return out


def deserialize_json(data: list) -> Indicators:
    import aws_sdk_detective.types.indicator

    out: Indicators = []
    for item in data:
        out.append(aws_sdk_detective.types.indicator.deserialize_json(item))
    return out
