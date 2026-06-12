"""Generated from Smithy shape ``com.amazonaws.networkmanager#AttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment

AttachmentList: TypeAlias = list["aws_sdk_networkmanager.types.attachment.Attachment"]


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentList) -> list:
    import aws_sdk_networkmanager.types.attachment

    out: list = []
    for item in value:
        out.append(aws_sdk_networkmanager.types.attachment.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttachmentList:
    import aws_sdk_networkmanager.types.attachment

    out: AttachmentList = []
    for item in data:
        out.append(aws_sdk_networkmanager.types.attachment.deserialize_json(item))
    return out
