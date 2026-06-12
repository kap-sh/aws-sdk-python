"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#FeatureType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

FeatureType: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: FeatureType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeatureType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FeatureType value: {data!r}")
    return cast(FeatureType, data)
