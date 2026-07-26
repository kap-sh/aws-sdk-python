"""Generated from Smithy shape ``com.amazonaws.glue#DataOperation``."""

from typing import Literal, TypeAlias, cast

DataOperation: TypeAlias = Literal[
    "READ",
    "WRITE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataOperation:
    return cast(DataOperation, data)
