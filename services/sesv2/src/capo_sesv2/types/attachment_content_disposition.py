"""Generated from Smithy shape ``com.amazonaws.sesv2#AttachmentContentDisposition``."""

from typing import Literal, TypeAlias, cast

AttachmentContentDisposition: TypeAlias = Literal[
    "ATTACHMENT",
    "INLINE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentContentDisposition) -> str:
    return value


def deserialize_json(data: str) -> AttachmentContentDisposition:
    return cast(AttachmentContentDisposition, data)
