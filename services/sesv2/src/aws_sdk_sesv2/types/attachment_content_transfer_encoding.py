"""Generated from Smithy shape ``com.amazonaws.sesv2#AttachmentContentTransferEncoding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

AttachmentContentTransferEncoding: TypeAlias = Literal[
    "BASE64",
    "QUOTED_PRINTABLE",
    "SEVEN_BIT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASE64",
        "QUOTED_PRINTABLE",
        "SEVEN_BIT",
    )
)


def serialize_json(value: AttachmentContentTransferEncoding) -> str:
    return value


def deserialize_json(data: str) -> AttachmentContentTransferEncoding:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AttachmentContentTransferEncoding value: {data!r}"
        )
    return cast(AttachmentContentTransferEncoding, data)
