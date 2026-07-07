"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ThemeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.theme_values_list


class ThemeValue(TypedDict, closed=True):
    value: NotRequired["str"]
    """<p>The value of a theme property.</p>"""
    children: NotRequired[
        "aws_sdk_amplifyuibuilder.types.theme_values_list.ThemeValuesList"
    ]
    """<p>A list of key-value pairs that define the theme's properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThemeValue) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    if "children" in value:
        import aws_sdk_amplifyuibuilder.types.theme_values_list

        out["children"] = (
            aws_sdk_amplifyuibuilder.types.theme_values_list.serialize_json(
                value["children"]
            )
        )
    return out


def deserialize_json(data: dict) -> ThemeValue:
    out: ThemeValue = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    if "children" in data:
        import aws_sdk_amplifyuibuilder.types.theme_values_list

        out["children"] = (
            aws_sdk_amplifyuibuilder.types.theme_values_list.deserialize_json(
                data["children"]
            )
        )
    return out
