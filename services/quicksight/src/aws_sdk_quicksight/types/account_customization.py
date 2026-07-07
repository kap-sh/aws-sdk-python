"""Generated from Smithy shape ``com.amazonaws.quicksight#AccountCustomization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn


class AccountCustomization(TypedDict, closed=True):
    default_theme: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The default theme for this Quick Sight subscription.</p>"""
    default_email_customization_template: NotRequired[
        "aws_sdk_quicksight.types.arn.Arn"
    ]
    """<p>The default email customization template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountCustomization) -> dict:
    out: dict = {}
    if "default_theme" in value:
        out["DefaultTheme"] = value["default_theme"]
    if "default_email_customization_template" in value:
        out["DefaultEmailCustomizationTemplate"] = value[
            "default_email_customization_template"
        ]
    return out


def deserialize_json(data: dict) -> AccountCustomization:
    out: AccountCustomization = {}  # type: ignore[typeddict-item]
    if "DefaultTheme" in data:
        out["default_theme"] = data["DefaultTheme"]
    if "DefaultEmailCustomizationTemplate" in data:
        out["default_email_customization_template"] = data[
            "DefaultEmailCustomizationTemplate"
        ]
    return out
