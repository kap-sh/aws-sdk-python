"""Generated from Smithy shape ``com.amazonaws.datazone#SortFieldConnection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

SortFieldConnection: TypeAlias = Literal["NAME",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("NAME",))


def serialize_json(value: SortFieldConnection) -> str:
    return value


def deserialize_json(data: str) -> SortFieldConnection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortFieldConnection value: {data!r}")
    return cast(SortFieldConnection, data)
