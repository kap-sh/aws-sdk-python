"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#TableStatus``."""

from typing import Literal, TypeAlias, cast

TableStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
    "RESTORING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TableStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TableStatus:
    return cast(TableStatus, data)
