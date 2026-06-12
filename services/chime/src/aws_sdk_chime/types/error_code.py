"""Generated from Smithy shape ``com.amazonaws.chime#ErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime.errors import DeserializationError

ErrorCode: TypeAlias = Literal[
    "BadRequest",
    "Conflict",
    "Forbidden",
    "NotFound",
    "PreconditionFailed",
    "ResourceLimitExceeded",
    "ServiceFailure",
    "AccessDenied",
    "ServiceUnavailable",
    "Throttled",
    "Throttling",
    "Unauthorized",
    "Unprocessable",
    "VoiceConnectorGroupAssociationsExist",
    "PhoneNumberAssociationsExist",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BadRequest",
        "Conflict",
        "Forbidden",
        "NotFound",
        "PreconditionFailed",
        "ResourceLimitExceeded",
        "ServiceFailure",
        "AccessDenied",
        "ServiceUnavailable",
        "Throttled",
        "Throttling",
        "Unauthorized",
        "Unprocessable",
        "VoiceConnectorGroupAssociationsExist",
        "PhoneNumberAssociationsExist",
    )
)


def serialize_json(value: ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ErrorCode value: {data!r}")
    return cast(ErrorCode, data)
