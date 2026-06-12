"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttachmentsInput``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.attachment_input

AttachmentsInput: TypeAlias = list["aws_sdk_qbusiness.types.attachment_input.AttachmentInput"]


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentsInput) -> list:
    import aws_sdk_qbusiness.types.attachment_input
    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.attachment_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttachmentsInput:
    import aws_sdk_qbusiness.types.attachment_input
    out: AttachmentsInput = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.attachment_input.deserialize_json(item))
    return out