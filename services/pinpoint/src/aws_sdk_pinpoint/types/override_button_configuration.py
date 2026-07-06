"""Generated from Smithy shape ``com.amazonaws.pinpoint#OverrideButtonConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.button_action


class OverrideButtonConfiguration(TypedDict, closed=True):
    button_action: NotRequired["aws_sdk_pinpoint.types.button_action.ButtonAction"]
    """<p>Action triggered by the button.</p>"""
    link: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>Button destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OverrideButtonConfiguration) -> dict:
    out: dict = {}
    if "button_action" in value:
        import aws_sdk_pinpoint.types.button_action

        out["ButtonAction"] = aws_sdk_pinpoint.types.button_action.serialize_json(
            value["button_action"]
        )
    if "link" in value:
        out["Link"] = value["link"]
    return out


def deserialize_json(data: dict) -> OverrideButtonConfiguration:
    out: OverrideButtonConfiguration = {}  # type: ignore[typeddict-item]
    if "ButtonAction" in data:
        import aws_sdk_pinpoint.types.button_action

        out["button_action"] = aws_sdk_pinpoint.types.button_action.deserialize_json(
            data["ButtonAction"]
        )
    if "Link" in data:
        out["link"] = data["Link"]
    return out
