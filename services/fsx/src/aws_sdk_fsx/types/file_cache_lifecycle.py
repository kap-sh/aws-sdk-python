"""Generated from Smithy shape ``com.amazonaws.fsx#FileCacheLifecycle``."""

from typing import Literal, TypeAlias, cast

FileCacheLifecycle: TypeAlias = Literal[
    "AVAILABLE",
    "CREATING",
    "DELETING",
    "UPDATING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileCacheLifecycle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileCacheLifecycle:
    return cast(FileCacheLifecycle, data)
