"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ErrorCode``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ErrorCode:
    return cast(ErrorCode, data)
