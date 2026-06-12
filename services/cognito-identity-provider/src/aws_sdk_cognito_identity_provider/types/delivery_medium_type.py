"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeliveryMediumType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

DeliveryMediumType: TypeAlias = Literal[
    "SMS",
    "EMAIL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SMS",
        "EMAIL",
    )
)


def serialize_aws_json_1_1(value: DeliveryMediumType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliveryMediumType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeliveryMediumType value: {data!r}")
    return cast(DeliveryMediumType, data)
