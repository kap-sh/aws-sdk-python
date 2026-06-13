"""Generated from Smithy shape ``com.amazonaws.odb#DbServerPatchingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

DbServerPatchingStatus: TypeAlias = Literal[
    "COMPLETE",
    "FAILED",
    "MAINTENANCE_IN_PROGRESS",
    "SCHEDULED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETE",
        "FAILED",
        "MAINTENANCE_IN_PROGRESS",
        "SCHEDULED",
    )
)


def serialize_aws_json_1_0(value: DbServerPatchingStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DbServerPatchingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DbServerPatchingStatus value: {data!r}")
    return cast(DbServerPatchingStatus, data)
