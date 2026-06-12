"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DomainStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

DomainStatusType: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "UPDATING",
    "ACTIVE",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "DELETING",
        "UPDATING",
        "ACTIVE",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: DomainStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DomainStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainStatusType value: {data!r}")
    return cast(DomainStatusType, data)
