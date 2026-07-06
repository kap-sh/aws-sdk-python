"""Generated from Smithy shape ``com.amazonaws.quicksight#ConditionalFormattingIconDisplayConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.conditional_formatting_icon_display_option


class ConditionalFormattingIconDisplayConfiguration(TypedDict, closed=True):
    icon_display_option: NotRequired[
        "aws_sdk_quicksight.types.conditional_formatting_icon_display_option.ConditionalFormattingIconDisplayOption"
    ]
    """<p>Determines the icon display configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalFormattingIconDisplayConfiguration) -> dict:
    out: dict = {}
    if "icon_display_option" in value:
        import aws_sdk_quicksight.types.conditional_formatting_icon_display_option

        out["IconDisplayOption"] = (
            aws_sdk_quicksight.types.conditional_formatting_icon_display_option.serialize_json(
                value["icon_display_option"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConditionalFormattingIconDisplayConfiguration:
    out: ConditionalFormattingIconDisplayConfiguration = {}  # type: ignore[typeddict-item]
    if "IconDisplayOption" in data:
        import aws_sdk_quicksight.types.conditional_formatting_icon_display_option

        out["icon_display_option"] = (
            aws_sdk_quicksight.types.conditional_formatting_icon_display_option.deserialize_json(
                data["IconDisplayOption"]
            )
        )
    return out
