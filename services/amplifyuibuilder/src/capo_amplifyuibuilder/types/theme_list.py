"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ThemeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.theme

ThemeList: TypeAlias = list["capo_amplifyuibuilder.types.theme.Theme"]


# --- restJson1 ser/de ---
def serialize_json(value: ThemeList) -> list:
    import capo_amplifyuibuilder.types.theme

    out: list = []
    for item in value:
        out.append(capo_amplifyuibuilder.types.theme.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThemeList:
    import capo_amplifyuibuilder.types.theme

    out: ThemeList = []
    for item in data:
        out.append(capo_amplifyuibuilder.types.theme.deserialize_json(item))
    return out
