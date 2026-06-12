"""Generated from Smithy shape ``com.amazonaws.rekognition#DatasetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

DatasetStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED",
    "DELETE_IN_PROGRESS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_IN_PROGRESS",
        "CREATE_COMPLETE",
        "CREATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_COMPLETE",
        "UPDATE_FAILED",
        "DELETE_IN_PROGRESS",
    )
)


def serialize_aws_json_1_1(value: DatasetStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatasetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatasetStatus value: {data!r}")
    return cast(DatasetStatus, data)
