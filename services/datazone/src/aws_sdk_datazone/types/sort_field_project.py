"""Generated from Smithy shape ``com.amazonaws.datazone#SortFieldProject``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

SortFieldProject: TypeAlias = Literal["NAME",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("NAME",))


def serialize_json(value: SortFieldProject) -> str:
    return value


def deserialize_json(data: str) -> SortFieldProject:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortFieldProject value: {data!r}")
    return cast(SortFieldProject, data)
