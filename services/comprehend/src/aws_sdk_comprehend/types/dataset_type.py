"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

DatasetType: TypeAlias = Literal[
    "TRAIN",
    "TEST",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRAIN",
        "TEST",
    )
)


def serialize_aws_json_1_1(value: DatasetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatasetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatasetType value: {data!r}")
    return cast(DatasetType, data)
