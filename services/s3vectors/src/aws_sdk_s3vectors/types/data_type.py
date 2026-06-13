"""Generated from Smithy shape ``com.amazonaws.s3vectors#DataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3vectors.errors import DeserializationError

DataType: TypeAlias = Literal["float32",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("float32",))


def serialize_json(value: DataType) -> str:
    return value


def deserialize_json(data: str) -> DataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataType value: {data!r}")
    return cast(DataType, data)
