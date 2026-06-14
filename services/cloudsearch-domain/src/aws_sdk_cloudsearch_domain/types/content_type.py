"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#ContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudsearch_domain.errors import DeserializationError

ContentType: TypeAlias = Literal[
    "application/json",
    "application/xml",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "application/json",
        "application/xml",
    )
)


def serialize_json(value: ContentType) -> str:
    return value


def deserialize_json(data: str) -> ContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentType value: {data!r}")
    return cast(ContentType, data)
