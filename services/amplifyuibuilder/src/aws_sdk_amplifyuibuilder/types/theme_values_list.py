"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ThemeValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.theme_values

ThemeValuesList: TypeAlias = list[
    "aws_sdk_amplifyuibuilder.types.theme_values.ThemeValues"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThemeValuesList) -> list:
    import aws_sdk_amplifyuibuilder.types.theme_values

    out: list = []
    for item in value:
        out.append(aws_sdk_amplifyuibuilder.types.theme_values.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThemeValuesList:
    import aws_sdk_amplifyuibuilder.types.theme_values

    out: ThemeValuesList = []
    for item in data:
        out.append(aws_sdk_amplifyuibuilder.types.theme_values.deserialize_json(item))
    return out
