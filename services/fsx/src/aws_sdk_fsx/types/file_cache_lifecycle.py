"""Generated from Smithy shape ``com.amazonaws.fsx#FileCacheLifecycle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

FileCacheLifecycle: TypeAlias = Literal[
    "AVAILABLE",
    "CREATING",
    "DELETING",
    "UPDATING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "CREATING",
        "DELETING",
        "UPDATING",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: FileCacheLifecycle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileCacheLifecycle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileCacheLifecycle value: {data!r}")
    return cast(FileCacheLifecycle, data)
