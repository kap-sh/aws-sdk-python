"""Generated from Smithy shape ``com.amazonaws.entityresolution#IncrementalRunType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_entityresolution.errors import DeserializationError

IncrementalRunType: TypeAlias = Literal["IMMEDIATE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("IMMEDIATE",))


def serialize_json(value: IncrementalRunType) -> str:
    return value


def deserialize_json(data: str) -> IncrementalRunType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IncrementalRunType value: {data!r}")
    return cast(IncrementalRunType, data)
