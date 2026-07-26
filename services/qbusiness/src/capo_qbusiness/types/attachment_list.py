"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.attachment

AttachmentList: TypeAlias = list["capo_qbusiness.types.attachment.Attachment"]


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentList) -> list:
    import capo_qbusiness.types.attachment

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.attachment.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttachmentList:
    import capo_qbusiness.types.attachment

    out: AttachmentList = []
    for item in data:
        out.append(capo_qbusiness.types.attachment.deserialize_json(item))
    return out
