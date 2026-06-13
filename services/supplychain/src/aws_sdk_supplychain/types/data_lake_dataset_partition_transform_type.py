"""Generated from Smithy shape ``com.amazonaws.supplychain#DataLakeDatasetPartitionTransformType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_supplychain.errors import DeserializationError

DataLakeDatasetPartitionTransformType: TypeAlias = Literal[
    "YEAR",
    "MONTH",
    "DAY",
    "HOUR",
    "IDENTITY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "YEAR",
        "MONTH",
        "DAY",
        "HOUR",
        "IDENTITY",
    )
)


def serialize_json(value: DataLakeDatasetPartitionTransformType) -> str:
    return value


def deserialize_json(data: str) -> DataLakeDatasetPartitionTransformType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataLakeDatasetPartitionTransformType value: {data!r}"
        )
    return cast(DataLakeDatasetPartitionTransformType, data)
