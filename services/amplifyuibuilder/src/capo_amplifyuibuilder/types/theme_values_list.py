"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ThemeValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.theme_values

ThemeValuesList: TypeAlias = list[
    "capo_amplifyuibuilder.types.theme_values.ThemeValues"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThemeValuesList) -> list:
    import capo_amplifyuibuilder.types.theme_values

    out: list = []
    for item in value:
        out.append(capo_amplifyuibuilder.types.theme_values.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThemeValuesList:
    import capo_amplifyuibuilder.types.theme_values

    out: ThemeValuesList = []
    for item in data:
        out.append(capo_amplifyuibuilder.types.theme_values.deserialize_json(item))
    return out
