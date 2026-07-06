"""Generated from Smithy shape ``com.amazonaws.qbusiness#ContentBlockerRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.system_message_override


class ContentBlockerRule(TypedDict, closed=True):
    system_message_override: NotRequired[
        "aws_sdk_qbusiness.types.system_message_override.SystemMessageOverride"
    ]
    """<p>The configured custom message displayed to an end user informing them that they've used a blocked phrase during chat.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlockerRule) -> dict:
    out: dict = {}
    if "system_message_override" in value:
        out["systemMessageOverride"] = value["system_message_override"]
    return out


def deserialize_json(data: dict) -> ContentBlockerRule:
    out: ContentBlockerRule = {}  # type: ignore[typeddict-item]
    if "systemMessageOverride" in data:
        out["system_message_override"] = data["systemMessageOverride"]
    return out
