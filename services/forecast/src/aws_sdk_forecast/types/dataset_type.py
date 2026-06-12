"""Generated from Smithy shape ``com.amazonaws.forecast#DatasetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_forecast.errors import DeserializationError

DatasetType: TypeAlias = Literal[
    "TARGET_TIME_SERIES",
    "RELATED_TIME_SERIES",
    "ITEM_METADATA",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TARGET_TIME_SERIES",
        "RELATED_TIME_SERIES",
        "ITEM_METADATA",
    )
)


def serialize_aws_json_1_1(value: DatasetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatasetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatasetType value: {data!r}")
    return cast(DatasetType, data)
