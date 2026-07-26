"""Generated from Smithy shape ``com.amazonaws.sesv2#AttachmentContentTransferEncoding``."""

from typing import Literal, TypeAlias, cast

AttachmentContentTransferEncoding: TypeAlias = Literal[
    "BASE64",
    "QUOTED_PRINTABLE",
    "SEVEN_BIT",
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentContentTransferEncoding) -> str:
    return value


def deserialize_json(data: str) -> AttachmentContentTransferEncoding:
    return cast(AttachmentContentTransferEncoding, data)
