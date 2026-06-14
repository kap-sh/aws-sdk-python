"""Generated from Smithy shape ``com.amazonaws.datazone#SortFieldAccountPool``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

SortFieldAccountPool: TypeAlias = Literal["NAME",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("NAME",))


def serialize_json(value: SortFieldAccountPool) -> str:
    return value


def deserialize_json(data: str) -> SortFieldAccountPool:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortFieldAccountPool value: {data!r}")
    return cast(SortFieldAccountPool, data)
