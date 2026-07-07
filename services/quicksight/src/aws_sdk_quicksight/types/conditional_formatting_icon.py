"""Generated from Smithy shape ``com.amazonaws.quicksight#ConditionalFormattingIcon``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.conditional_formatting_custom_icon_condition
    import aws_sdk_quicksight.types.conditional_formatting_icon_set


class ConditionalFormattingIcon(TypedDict, closed=True):
    icon_set: NotRequired[
        "aws_sdk_quicksight.types.conditional_formatting_icon_set.ConditionalFormattingIconSet"
    ]
    """<p>Formatting configuration for icon set.</p>"""
    custom_condition: NotRequired[
        "aws_sdk_quicksight.types.conditional_formatting_custom_icon_condition.ConditionalFormattingCustomIconCondition"
    ]
    """<p>Determines the custom condition for an icon set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalFormattingIcon) -> dict:
    out: dict = {}
    if "icon_set" in value:
        import aws_sdk_quicksight.types.conditional_formatting_icon_set

        out["IconSet"] = (
            aws_sdk_quicksight.types.conditional_formatting_icon_set.serialize_json(
                value["icon_set"]
            )
        )
    if "custom_condition" in value:
        import aws_sdk_quicksight.types.conditional_formatting_custom_icon_condition

        out["CustomCondition"] = (
            aws_sdk_quicksight.types.conditional_formatting_custom_icon_condition.serialize_json(
                value["custom_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConditionalFormattingIcon:
    out: ConditionalFormattingIcon = {}  # type: ignore[typeddict-item]
    if "IconSet" in data:
        import aws_sdk_quicksight.types.conditional_formatting_icon_set

        out["icon_set"] = (
            aws_sdk_quicksight.types.conditional_formatting_icon_set.deserialize_json(
                data["IconSet"]
            )
        )
    if "CustomCondition" in data:
        import aws_sdk_quicksight.types.conditional_formatting_custom_icon_condition

        out["custom_condition"] = (
            aws_sdk_quicksight.types.conditional_formatting_custom_icon_condition.deserialize_json(
                data["CustomCondition"]
            )
        )
    return out
