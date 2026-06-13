"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetImportMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DataSetImportMode: TypeAlias = Literal[
    "SPICE",
    "DIRECT_QUERY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SPICE",
        "DIRECT_QUERY",
    )
)


def serialize_json(value: DataSetImportMode) -> str:
    return value


def deserialize_json(data: str) -> DataSetImportMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSetImportMode value: {data!r}")
    return cast(DataSetImportMode, data)
