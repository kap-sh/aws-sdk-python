"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DatastoreStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medical_imaging.errors import DeserializationError

DatastoreStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "ACTIVE",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATE_FAILED",
        "ACTIVE",
        "DELETING",
        "DELETED",
    )
)


def serialize_json(value: DatastoreStatus) -> str:
    return value


def deserialize_json(data: str) -> DatastoreStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatastoreStatus value: {data!r}")
    return cast(DatastoreStatus, data)
