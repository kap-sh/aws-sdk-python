"""Generated from Smithy shape ``com.amazonaws.quicksight#GradientStopList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.gradient_stop

GradientStopList: TypeAlias = list[
    "aws_sdk_quicksight.types.gradient_stop.GradientStop"
]


# --- restJson1 ser/de ---
def serialize_json(value: GradientStopList) -> list:
    import aws_sdk_quicksight.types.gradient_stop

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.gradient_stop.serialize_json(item))
    return out


def deserialize_json(data: list) -> GradientStopList:
    import aws_sdk_quicksight.types.gradient_stop

    out: GradientStopList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.gradient_stop.deserialize_json(item))
    return out
