"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomColorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.custom_color

CustomColorsList: TypeAlias = list["aws_sdk_quicksight.types.custom_color.CustomColor"]


# --- restJson1 ser/de ---
def serialize_json(value: CustomColorsList) -> list:
    import aws_sdk_quicksight.types.custom_color

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.custom_color.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomColorsList:
    import aws_sdk_quicksight.types.custom_color

    out: CustomColorsList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.custom_color.deserialize_json(item))
    return out
