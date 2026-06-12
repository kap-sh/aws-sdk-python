"""Generated from Smithy shape ``com.amazonaws.connect#DataTableStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

DataTableStatus: TypeAlias = Literal["PUBLISHED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PUBLISHED",))


def serialize_json(value: DataTableStatus) -> str:
    return value


def deserialize_json(data: str) -> DataTableStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataTableStatus value: {data!r}")
    return cast(DataTableStatus, data)
