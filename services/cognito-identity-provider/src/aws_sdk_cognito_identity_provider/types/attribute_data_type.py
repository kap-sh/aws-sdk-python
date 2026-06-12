"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AttributeDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

AttributeDataType: TypeAlias = Literal[
    "String",
    "Number",
    "DateTime",
    "Boolean",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "String",
        "Number",
        "DateTime",
        "Boolean",
    )
)


def serialize_aws_json_1_1(value: AttributeDataType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AttributeDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttributeDataType value: {data!r}")
    return cast(AttributeDataType, data)
