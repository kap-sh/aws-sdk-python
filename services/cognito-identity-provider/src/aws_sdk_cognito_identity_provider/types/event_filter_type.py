"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#EventFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

EventFilterType: TypeAlias = Literal[
    "SIGN_IN",
    "PASSWORD_CHANGE",
    "SIGN_UP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SIGN_IN",
        "PASSWORD_CHANGE",
        "SIGN_UP",
    )
)


def serialize_aws_json_1_1(value: EventFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventFilterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventFilterType value: {data!r}")
    return cast(EventFilterType, data)
