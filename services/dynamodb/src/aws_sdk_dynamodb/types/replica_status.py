"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb.errors import DeserializationError

ReplicaStatus: TypeAlias = Literal[
    "CREATING",
    "CREATION_FAILED",
    "UPDATING",
    "DELETING",
    "ACTIVE",
    "REGION_DISABLED",
    "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
    "ARCHIVING",
    "ARCHIVED",
    "REPLICATION_NOT_AUTHORIZED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATION_FAILED",
        "UPDATING",
        "DELETING",
        "ACTIVE",
        "REGION_DISABLED",
        "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
        "ARCHIVING",
        "ARCHIVED",
        "REPLICATION_NOT_AUTHORIZED",
    )
)


def serialize_aws_json_1_0(value: ReplicaStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ReplicaStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReplicaStatus value: {data!r}")
    return cast(ReplicaStatus, data)
