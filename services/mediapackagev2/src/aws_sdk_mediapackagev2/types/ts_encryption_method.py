"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#TsEncryptionMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

TsEncryptionMethod: TypeAlias = Literal[
    "AES_128",
    "SAMPLE_AES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AES_128",
        "SAMPLE_AES",
    )
)


def serialize_json(value: TsEncryptionMethod) -> str:
    return value


def deserialize_json(data: str) -> TsEncryptionMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TsEncryptionMethod value: {data!r}")
    return cast(TsEncryptionMethod, data)
