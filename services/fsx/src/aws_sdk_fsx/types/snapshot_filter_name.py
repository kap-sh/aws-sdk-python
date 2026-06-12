"""Generated from Smithy shape ``com.amazonaws.fsx#SnapshotFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

SnapshotFilterName: TypeAlias = Literal[
    "file-system-id",
    "volume-id",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "file-system-id",
        "volume-id",
    )
)


def serialize_aws_json_1_1(value: SnapshotFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnapshotFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SnapshotFilterName value: {data!r}")
    return cast(SnapshotFilterName, data)
