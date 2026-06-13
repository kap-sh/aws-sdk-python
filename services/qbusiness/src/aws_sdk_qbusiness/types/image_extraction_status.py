"""Generated from Smithy shape ``com.amazonaws.qbusiness#ImageExtractionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

ImageExtractionStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: ImageExtractionStatus) -> str:
    return value


def deserialize_json(data: str) -> ImageExtractionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageExtractionStatus value: {data!r}")
    return cast(ImageExtractionStatus, data)
