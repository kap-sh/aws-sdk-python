"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DatastoreStatus``."""

from typing import Literal, TypeAlias, cast

DatastoreStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "ACTIVE",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DatastoreStatus) -> str:
    return value


def deserialize_json(data: str) -> DatastoreStatus:
    return cast(DatastoreStatus, data)
