"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#IssuerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

IssuerType: TypeAlias = Literal[
    "ORIGINAL",
    "UPDATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ORIGINAL",
        "UPDATED",
    )
)


def serialize_aws_json_1_1(value: IssuerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IssuerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IssuerType value: {data!r}")
    return cast(IssuerType, data)
