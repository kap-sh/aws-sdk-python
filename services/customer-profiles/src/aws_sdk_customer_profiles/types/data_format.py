"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DataFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

DataFormat: TypeAlias = Literal[
    "CSV",
    "JSONL",
    "ORC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CSV",
        "JSONL",
        "ORC",
    )
)


def serialize_json(value: DataFormat) -> str:
    return value


def deserialize_json(data: str) -> DataFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataFormat value: {data!r}")
    return cast(DataFormat, data)
