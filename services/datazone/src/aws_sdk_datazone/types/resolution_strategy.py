"""Generated from Smithy shape ``com.amazonaws.datazone#ResolutionStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

ResolutionStrategy: TypeAlias = Literal["MANUAL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MANUAL",))


def serialize_json(value: ResolutionStrategy) -> str:
    return value


def deserialize_json(data: str) -> ResolutionStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResolutionStrategy value: {data!r}")
    return cast(ResolutionStrategy, data)
