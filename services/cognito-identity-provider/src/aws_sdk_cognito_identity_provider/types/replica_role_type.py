"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ReplicaRoleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

ReplicaRoleType: TypeAlias = Literal[
    "PRIMARY",
    "SECONDARY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIMARY",
        "SECONDARY",
    )
)


def serialize_aws_json_1_1(value: ReplicaRoleType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReplicaRoleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReplicaRoleType value: {data!r}")
    return cast(ReplicaRoleType, data)
