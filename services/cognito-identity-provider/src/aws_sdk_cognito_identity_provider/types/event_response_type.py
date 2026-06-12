"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#EventResponseType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

EventResponseType: TypeAlias = Literal[
    "Pass",
    "Fail",
    "InProgress",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pass",
        "Fail",
        "InProgress",
    )
)


def serialize_aws_json_1_1(value: EventResponseType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventResponseType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventResponseType value: {data!r}")
    return cast(EventResponseType, data)
