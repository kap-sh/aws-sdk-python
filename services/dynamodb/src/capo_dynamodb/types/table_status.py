"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_0(value: TableStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TableStatus:
    return cast(TableStatus, data)
