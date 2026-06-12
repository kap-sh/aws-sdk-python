"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

ErrorCode: TypeAlias = Literal[
    "BadRequest",
    "Forbidden",
    "NotFound",
    "ResourceLimitExceeded",
    "ServiceFailure",
    "ServiceUnavailable",
    "Throttling",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BadRequest",
        "Forbidden",
        "NotFound",
        "ResourceLimitExceeded",
        "ServiceFailure",
        "ServiceUnavailable",
        "Throttling",
    )
)


def serialize_json(value: ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ErrorCode value: {data!r}")
    return cast(ErrorCode, data)
