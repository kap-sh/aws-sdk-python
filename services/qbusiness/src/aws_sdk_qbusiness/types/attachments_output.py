"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttachmentsOutput``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.attachment_output

AttachmentsOutput: TypeAlias = list["aws_sdk_qbusiness.types.attachment_output.AttachmentOutput"]


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentsOutput) -> list:
    import aws_sdk_qbusiness.types.attachment_output
    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.attachment_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttachmentsOutput:
    import aws_sdk_qbusiness.types.attachment_output
    out: AttachmentsOutput = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.attachment_output.deserialize_json(item))
    return out