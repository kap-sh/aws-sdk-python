"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryLifecycle``."""

from typing import Literal, TypeAlias, cast

DataRepositoryLifecycle: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "MISCONFIGURED",
    "UPDATING",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataRepositoryLifecycle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataRepositoryLifecycle:
    return cast(DataRepositoryLifecycle, data)
