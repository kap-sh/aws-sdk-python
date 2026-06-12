"""Generated from Smithy shape ``com.amazonaws.fsx#SnapshotLifecycle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

SnapshotLifecycle: TypeAlias = Literal[
    "PENDING",
    "CREATING",
    "DELETING",
    "AVAILABLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "CREATING",
        "DELETING",
        "AVAILABLE",
    )
)


def serialize_aws_json_1_1(value: SnapshotLifecycle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotLifecycle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SnapshotLifecycle value: {data!r}")
    return cast(SnapshotLifecycle, data)
