"""Generated from Smithy shape ``com.amazonaws.cognitosync#Platform``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_sync.errors import DeserializationError

Platform: TypeAlias = Literal[
    "APNS",
    "APNS_SANDBOX",
    "GCM",
    "ADM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APNS",
        "APNS_SANDBOX",
        "GCM",
        "ADM",
    )
)


def serialize_json(value: Platform) -> str:
    return value


def deserialize_json(data: str) -> Platform:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Platform value: {data!r}")
    return cast(Platform, data)
