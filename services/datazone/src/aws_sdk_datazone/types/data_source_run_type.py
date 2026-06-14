"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceRunType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

DataSourceRunType: TypeAlias = Literal[
    "PRIORITIZED",
    "SCHEDULED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIORITIZED",
        "SCHEDULED",
    )
)


def serialize_json(value: DataSourceRunType) -> str:
    return value


def deserialize_json(data: str) -> DataSourceRunType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSourceRunType value: {data!r}")
    return cast(DataSourceRunType, data)
