"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceUserEndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_identity.errors import DeserializationError

AppInstanceUserEndpointType: TypeAlias = Literal[
    "APNS",
    "APNS_SANDBOX",
    "GCM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APNS",
        "APNS_SANDBOX",
        "GCM",
    )
)


def serialize_json(value: AppInstanceUserEndpointType) -> str:
    return value


def deserialize_json(data: str) -> AppInstanceUserEndpointType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AppInstanceUserEndpointType value: {data!r}"
        )
    return cast(AppInstanceUserEndpointType, data)
