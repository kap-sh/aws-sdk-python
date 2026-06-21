"""Generated from Smithy shape ``com.amazonaws.workspaces#DataReplication``."""

from typing import Literal, TypeAlias, cast

DataReplication: TypeAlias = Literal[
    "NO_REPLICATION",
    "PRIMARY_AS_SOURCE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataReplication) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataReplication:
    return cast(DataReplication, data)
