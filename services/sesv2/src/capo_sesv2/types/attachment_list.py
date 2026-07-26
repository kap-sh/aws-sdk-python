"""Generated from Smithy shape ``com.amazonaws.sesv2#AttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.attachment

AttachmentList: TypeAlias = list["capo_sesv2.types.attachment.Attachment"]


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentList) -> list:
    import capo_sesv2.types.attachment

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.attachment.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttachmentList:
    import capo_sesv2.types.attachment

    out: AttachmentList = []
    for item in data:
        out.append(capo_sesv2.types.attachment.deserialize_json(item))
    return out
