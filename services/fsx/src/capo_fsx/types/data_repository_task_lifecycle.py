"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryTaskLifecycle``."""

from typing import Literal, TypeAlias, cast

DataRepositoryTaskLifecycle: TypeAlias = Literal[
    "PENDING",
    "EXECUTING",
    "FAILED",
    "SUCCEEDED",
    "CANCELED",
    "CANCELING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataRepositoryTaskLifecycle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataRepositoryTaskLifecycle:
    return cast(DataRepositoryTaskLifecycle, data)
