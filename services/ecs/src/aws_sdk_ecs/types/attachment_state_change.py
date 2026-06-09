"""Generated from Smithy shape ``com.amazonaws.ecs#AttachmentStateChange``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class AttachmentStateChange(TypedDict):
    attachment_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the attachment.</p>"""
    status: "aws_sdk_ecs.types.string.String"
    """<p>The status of the attachment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentStateChange) -> dict:
    out: dict = {}
    out["attachmentArn"] = value["attachment_arn"]
    out["status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachmentStateChange:
    out: AttachmentStateChange = {}  # type: ignore[typeddict-item]
    if "attachmentArn" in data:
        out["attachment_arn"] = data["attachmentArn"]
    else:
        raise DeserializationError("AttachmentStateChange.attachment_arn required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("AttachmentStateChange.status required")
    return out
