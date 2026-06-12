"""Generated from Smithy shape ``com.amazonaws.sesv2#AttachmentContentDisposition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

AttachmentContentDisposition: TypeAlias = Literal[
    "ATTACHMENT",
    "INLINE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ATTACHMENT",
        "INLINE",
    )
)


def serialize_json(value: AttachmentContentDisposition) -> str:
    return value


def deserialize_json(data: str) -> AttachmentContentDisposition:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AttachmentContentDisposition value: {data!r}"
        )
    return cast(AttachmentContentDisposition, data)
