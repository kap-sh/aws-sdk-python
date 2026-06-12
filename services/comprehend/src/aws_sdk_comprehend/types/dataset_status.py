"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

DatasetStatus: TypeAlias = Literal[
    "CREATING",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: DatasetStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatasetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatasetStatus value: {data!r}")
    return cast(DatasetStatus, data)
