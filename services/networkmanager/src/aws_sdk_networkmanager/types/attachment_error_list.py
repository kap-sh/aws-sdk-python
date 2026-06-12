"""Generated from Smithy shape ``com.amazonaws.networkmanager#AttachmentErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment_error

AttachmentErrorList: TypeAlias = list[
    "aws_sdk_networkmanager.types.attachment_error.AttachmentError"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentErrorList) -> list:
    import aws_sdk_networkmanager.types.attachment_error

    out: list = []
    for item in value:
        out.append(aws_sdk_networkmanager.types.attachment_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttachmentErrorList:
    import aws_sdk_networkmanager.types.attachment_error

    out: AttachmentErrorList = []
    for item in data:
        out.append(aws_sdk_networkmanager.types.attachment_error.deserialize_json(item))
    return out
