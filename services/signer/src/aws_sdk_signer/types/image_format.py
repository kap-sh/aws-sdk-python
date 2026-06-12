"""Generated from Smithy shape ``com.amazonaws.signer#ImageFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_signer.errors import DeserializationError

ImageFormat: TypeAlias = Literal[
    "JSON",
    "JSONEmbedded",
    "JSONDetached",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JSON",
        "JSONEmbedded",
        "JSONDetached",
    )
)


def serialize_json(value: ImageFormat) -> str:
    return value


def deserialize_json(data: str) -> ImageFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageFormat value: {data!r}")
    return cast(ImageFormat, data)
