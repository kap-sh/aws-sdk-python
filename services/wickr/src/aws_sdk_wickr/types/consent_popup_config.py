"""Generated from Smithy shape ``com.amazonaws.wickr#ConsentPopupConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string


class ConsentPopupConfig(TypedDict):
    enabled: "bool"
    """<p>Whether the consent popup is enabled. When set to true, the popup is displayed to users on login.</p>"""
    header: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>Header text displayed at the top of the consent popup. Maximum 100 characters.</p>"""
    content: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>Body content of the consent popup in Markdown format. Maximum 5000 characters.</p>"""
    close_button_label: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    r"""<p>Label for the close button on the consent popup. Maximum 20 characters. Defaults to \"Acknowledge\" if not provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConsentPopupConfig) -> dict:
    out: dict = {}
    out["enabled"] = value["enabled"]
    if "header" in value:
        out["header"] = value["header"]
    if "content" in value:
        out["content"] = value["content"]
    if "close_button_label" in value:
        out["closeButtonLabel"] = value["close_button_label"]
    return out


def deserialize_json(data: dict) -> ConsentPopupConfig:
    out: ConsentPopupConfig = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        raise DeserializationError("ConsentPopupConfig.enabled required")
    if "header" in data:
        out["header"] = data["header"]
    if "content" in data:
        out["content"] = data["content"]
    if "closeButtonLabel" in data:
        out["close_button_label"] = data["closeButtonLabel"]
    return out
