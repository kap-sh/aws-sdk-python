"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultFormatting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.display_format
    import aws_sdk_quicksight.types.display_format_options


class DefaultFormatting(TypedDict):
    display_format: NotRequired["aws_sdk_quicksight.types.display_format.DisplayFormat"]
    """<p>The display format. Valid values for this structure are <code>AUTO</code>, <code>PERCENT</code>, <code>CURRENCY</code>, <code>NUMBER</code>, <code>DATE</code>, and <code>STRING</code>.</p>"""
    display_format_options: NotRequired[
        "aws_sdk_quicksight.types.display_format_options.DisplayFormatOptions"
    ]
    """<p>The additional options for display formatting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultFormatting) -> dict:
    out: dict = {}
    if "display_format" in value:
        import aws_sdk_quicksight.types.display_format

        out["DisplayFormat"] = aws_sdk_quicksight.types.display_format.serialize_json(
            value["display_format"]
        )
    if "display_format_options" in value:
        import aws_sdk_quicksight.types.display_format_options

        out["DisplayFormatOptions"] = (
            aws_sdk_quicksight.types.display_format_options.serialize_json(
                value["display_format_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> DefaultFormatting:
    out: DefaultFormatting = {}  # type: ignore[typeddict-item]
    if "DisplayFormat" in data:
        import aws_sdk_quicksight.types.display_format

        out["display_format"] = (
            aws_sdk_quicksight.types.display_format.deserialize_json(
                data["DisplayFormat"]
            )
        )
    if "DisplayFormatOptions" in data:
        import aws_sdk_quicksight.types.display_format_options

        out["display_format_options"] = (
            aws_sdk_quicksight.types.display_format_options.deserialize_json(
                data["DisplayFormatOptions"]
            )
        )
    return out
