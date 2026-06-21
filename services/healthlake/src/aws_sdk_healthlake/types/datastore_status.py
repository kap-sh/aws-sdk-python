"""Generated from Smithy shape ``com.amazonaws.healthlake#DatastoreStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_0(value: DatastoreStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DatastoreStatus:
    return cast(DatastoreStatus, data)
