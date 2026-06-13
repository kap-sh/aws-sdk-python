"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetFilterAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DataSetFilterAttribute: TypeAlias = Literal[
    "QUICKSIGHT_VIEWER_OR_OWNER",
    "QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "DATASET_NAME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUICKSIGHT_VIEWER_OR_OWNER",
        "QUICKSIGHT_OWNER",
        "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
        "DIRECT_QUICKSIGHT_OWNER",
        "DIRECT_QUICKSIGHT_SOLE_OWNER",
        "DATASET_NAME",
    )
)


def serialize_json(value: DataSetFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> DataSetFilterAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSetFilterAttribute value: {data!r}")
    return cast(DataSetFilterAttribute, data)
