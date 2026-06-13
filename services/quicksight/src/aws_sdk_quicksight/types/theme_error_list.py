"""Generated from Smithy shape ``com.amazonaws.quicksight#ThemeErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.theme_error

ThemeErrorList: TypeAlias = list["aws_sdk_quicksight.types.theme_error.ThemeError"]


# --- restJson1 ser/de ---
def serialize_json(value: ThemeErrorList) -> list:
    import aws_sdk_quicksight.types.theme_error

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.theme_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThemeErrorList:
    import aws_sdk_quicksight.types.theme_error

    out: ThemeErrorList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.theme_error.deserialize_json(item))
    return out
