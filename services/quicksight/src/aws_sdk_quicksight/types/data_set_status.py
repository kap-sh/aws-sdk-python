"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DataSetStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "ACTIVE",
    "FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "ACTIVE",
        "FAILED",
        "DELETING",
    )
)


def serialize_json(value: DataSetStatus) -> str:
    return value


def deserialize_json(data: str) -> DataSetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSetStatus value: {data!r}")
    return cast(DataSetStatus, data)
