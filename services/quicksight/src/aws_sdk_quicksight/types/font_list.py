"""Generated from Smithy shape ``com.amazonaws.quicksight#FontList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.font

FontList: TypeAlias = list["aws_sdk_quicksight.types.font.Font"]


# --- restJson1 ser/de ---
def serialize_json(value: FontList) -> list:
    import aws_sdk_quicksight.types.font

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.font.serialize_json(item))
    return out


def deserialize_json(data: list) -> FontList:
    import aws_sdk_quicksight.types.font

    out: FontList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.font.deserialize_json(item))
    return out
