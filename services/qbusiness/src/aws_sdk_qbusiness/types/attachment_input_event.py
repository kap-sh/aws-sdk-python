"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttachmentInputEvent``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.attachment_input

class AttachmentInputEvent(TypedDict):
    attachment: NotRequired["aws_sdk_qbusiness.types.attachment_input.AttachmentInput"]

# --- restJson1 ser/de ---
def serialize_json(value: AttachmentInputEvent) -> dict:
    out: dict = {}
    if "attachment" in value:
        import aws_sdk_qbusiness.types.attachment_input
        out["attachment"] = aws_sdk_qbusiness.types.attachment_input.serialize_json(value["attachment"])
    return out


def deserialize_json(data: dict) -> AttachmentInputEvent:
    out: AttachmentInputEvent = {}  # type: ignore[typeddict-item]
    if "attachment" in data:
        import aws_sdk_qbusiness.types.attachment_input
        out["attachment"] = aws_sdk_qbusiness.types.attachment_input.deserialize_json(data["attachment"])
    return out