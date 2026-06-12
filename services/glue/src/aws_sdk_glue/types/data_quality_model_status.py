"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityModelStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

DataQualityModelStatus: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: DataQualityModelStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataQualityModelStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataQualityModelStatus value: {data!r}")
    return cast(DataQualityModelStatus, data)
