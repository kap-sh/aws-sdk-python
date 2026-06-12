"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ResourceSnapshotJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

ResourceSnapshotJobStatus: TypeAlias = Literal[
    "Running",
    "Stopped",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Running",
        "Stopped",
    )
)


def serialize_aws_json_1_0(value: ResourceSnapshotJobStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceSnapshotJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceSnapshotJobStatus value: {data!r}")
    return cast(ResourceSnapshotJobStatus, data)
