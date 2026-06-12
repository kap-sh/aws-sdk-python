"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#Message``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string


class Message(TypedDict):
    message_text: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The text of a readiness check message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Message) -> dict:
    out: dict = {}
    if "message_text" in value:
        out["messageText"] = value["message_text"]
    return out


def deserialize_json(data: dict) -> Message:
    out: Message = {}  # type: ignore[typeddict-item]
    if "messageText" in data:
        out["message_text"] = data["messageText"]
    return out
