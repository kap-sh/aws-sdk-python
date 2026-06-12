"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#EventSourceName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

EventSourceName: TypeAlias = Literal[
    "userNotification",
    "userAuthEvents",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "userNotification",
        "userAuthEvents",
    )
)


def serialize_aws_json_1_1(value: EventSourceName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventSourceName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventSourceName value: {data!r}")
    return cast(EventSourceName, data)
