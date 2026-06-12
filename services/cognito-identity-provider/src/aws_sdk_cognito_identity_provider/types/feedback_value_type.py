"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#FeedbackValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

FeedbackValueType: TypeAlias = Literal[
    "Valid",
    "Invalid",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Valid",
        "Invalid",
    )
)


def serialize_aws_json_1_1(value: FeedbackValueType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeedbackValueType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FeedbackValueType value: {data!r}")
    return cast(FeedbackValueType, data)
