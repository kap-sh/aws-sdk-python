"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#StatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

StatusType: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def serialize_aws_json_1_1(value: StatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatusType value: {data!r}")
    return cast(StatusType, data)
