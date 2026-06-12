"""Generated from Smithy shape ``com.amazonaws.healthlake#DatastoreStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_healthlake.errors import DeserializationError

DatastoreStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "DELETED",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "DELETING",
        "DELETED",
        "CREATE_FAILED",
        "UPDATING",
        "UPDATE_FAILED",
    )
)


def serialize_aws_json_1_0(value: DatastoreStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DatastoreStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatastoreStatus value: {data!r}")
    return cast(DatastoreStatus, data)
