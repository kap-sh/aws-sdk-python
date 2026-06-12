"""Generated from Smithy shape ``com.amazonaws.qbusiness#AppliedAttachmentsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.attachments_control_mode

class AppliedAttachmentsConfiguration(TypedDict):
    attachments_control_mode: NotRequired["aws_sdk_qbusiness.types.attachments_control_mode.AttachmentsControlMode"]
    """<p>Information about whether file upload during chat functionality is activated for your application.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AppliedAttachmentsConfiguration) -> dict:
    out: dict = {}
    if "attachments_control_mode" in value:
        import aws_sdk_qbusiness.types.attachments_control_mode
        out["attachmentsControlMode"] = aws_sdk_qbusiness.types.attachments_control_mode.serialize_json(value["attachments_control_mode"])
    return out


def deserialize_json(data: dict) -> AppliedAttachmentsConfiguration:
    out: AppliedAttachmentsConfiguration = {}  # type: ignore[typeddict-item]
    if "attachmentsControlMode" in data:
        import aws_sdk_qbusiness.types.attachments_control_mode
        out["attachments_control_mode"] = aws_sdk_qbusiness.types.attachments_control_mode.deserialize_json(data["attachmentsControlMode"])
    return out