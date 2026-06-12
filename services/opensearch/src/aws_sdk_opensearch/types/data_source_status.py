"""Generated from Smithy shape ``com.amazonaws.opensearch#DataSourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

DataSourceStatus: TypeAlias = Literal[
    "ACTIVE",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DISABLED",
    )
)


def serialize_json(value: DataSourceStatus) -> str:
    return value


def deserialize_json(data: str) -> DataSourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSourceStatus value: {data!r}")
    return cast(DataSourceStatus, data)
