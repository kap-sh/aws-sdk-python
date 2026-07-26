"""Generated from Smithy shape ``com.amazonaws.quicksight#ThemeErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.theme_error

ThemeErrorList: TypeAlias = list["capo_quicksight.types.theme_error.ThemeError"]


# --- restJson1 ser/de ---
def serialize_json(value: ThemeErrorList) -> list:
    import capo_quicksight.types.theme_error

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.theme_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThemeErrorList:
    import capo_quicksight.types.theme_error

    out: ThemeErrorList = []
    for item in data:
        out.append(capo_quicksight.types.theme_error.deserialize_json(item))
    return out
