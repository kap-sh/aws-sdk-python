"""Generated from Smithy shape ``com.amazonaws.quicksight#ThemeAliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.theme_alias

ThemeAliasList: TypeAlias = list["aws_sdk_quicksight.types.theme_alias.ThemeAlias"]


# --- restJson1 ser/de ---
def serialize_json(value: ThemeAliasList) -> list:
    import aws_sdk_quicksight.types.theme_alias

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.theme_alias.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThemeAliasList:
    import aws_sdk_quicksight.types.theme_alias

    out: ThemeAliasList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.theme_alias.deserialize_json(item))
    return out
