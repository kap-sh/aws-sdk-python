"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CmafEncryptionMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

CmafEncryptionMethod: TypeAlias = Literal[
    "CENC",
    "CBCS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CENC",
        "CBCS",
    )
)


def serialize_json(value: CmafEncryptionMethod) -> str:
    return value


def deserialize_json(data: str) -> CmafEncryptionMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CmafEncryptionMethod value: {data!r}")
    return cast(CmafEncryptionMethod, data)
