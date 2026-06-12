"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryLifecycle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

DataRepositoryLifecycle: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "MISCONFIGURED",
    "UPDATING",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "AVAILABLE",
        "MISCONFIGURED",
        "UPDATING",
        "DELETING",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: DataRepositoryLifecycle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataRepositoryLifecycle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataRepositoryLifecycle value: {data!r}")
    return cast(DataRepositoryLifecycle, data)
