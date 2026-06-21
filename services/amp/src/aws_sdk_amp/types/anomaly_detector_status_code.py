"""Generated from Smithy shape ``com.amazonaws.amp#AnomalyDetectorStatusCode``."""

from typing import Literal, TypeAlias, cast

AnomalyDetectorStatusCode: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "CREATION_FAILED",
    "UPDATE_FAILED",
    "DELETION_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnomalyDetectorStatusCode) -> str:
    return value


def deserialize_json(data: str) -> AnomalyDetectorStatusCode:
    return cast(AnomalyDetectorStatusCode, data)
