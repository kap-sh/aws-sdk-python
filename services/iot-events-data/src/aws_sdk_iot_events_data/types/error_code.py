"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#ErrorCode``."""

from typing import Literal, TypeAlias, cast

ErrorCode: TypeAlias = Literal[
    "ResourceNotFoundException",
    "InvalidRequestException",
    "InternalFailureException",
    "ServiceUnavailableException",
    "ThrottlingException",
]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ErrorCode:
    return cast(ErrorCode, data)
