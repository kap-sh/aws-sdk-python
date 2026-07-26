"""Generated from Smithy shape ``com.amazonaws.clouddirectory#IndexAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.index_attachment

IndexAttachmentList: TypeAlias = list[
    "capo_clouddirectory.types.index_attachment.IndexAttachment"
]


# --- restJson1 ser/de ---
def serialize_json(value: IndexAttachmentList) -> list:
    import capo_clouddirectory.types.index_attachment

    out: list = []
    for item in value:
        out.append(capo_clouddirectory.types.index_attachment.serialize_json(item))
    return out


def deserialize_json(data: list) -> IndexAttachmentList:
    import capo_clouddirectory.types.index_attachment

    out: IndexAttachmentList = []
    for item in data:
        out.append(capo_clouddirectory.types.index_attachment.deserialize_json(item))
    return out
