"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ReplicaStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

ReplicaStatusType: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "INACTIVE",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "INACTIVE",
        "DELETING",
    )
)


def serialize_aws_json_1_1(value: ReplicaStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReplicaStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReplicaStatusType value: {data!r}")
    return cast(ReplicaStatusType, data)
