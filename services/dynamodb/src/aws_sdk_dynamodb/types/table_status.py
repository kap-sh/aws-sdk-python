"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb.errors import DeserializationError

TableStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "ACTIVE",
    "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
    "ARCHIVING",
    "ARCHIVED",
    "REPLICATION_NOT_AUTHORIZED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "DELETING",
        "ACTIVE",
        "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
        "ARCHIVING",
        "ARCHIVED",
        "REPLICATION_NOT_AUTHORIZED",
    )
)


def serialize_aws_json_1_0(value: TableStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TableStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TableStatus value: {data!r}")
    return cast(TableStatus, data)
