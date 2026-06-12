"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateReplicaStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

UpdateReplicaStatusType: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_aws_json_1_1(value: UpdateReplicaStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpdateReplicaStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateReplicaStatusType value: {data!r}")
    return cast(UpdateReplicaStatusType, data)
