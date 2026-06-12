"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TraversalType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

TraversalType: TypeAlias = Literal["PATH_TO_ROOT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PATH_TO_ROOT",))


def serialize_json(value: TraversalType) -> str:
    return value


def deserialize_json(data: str) -> TraversalType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TraversalType value: {data!r}")
    return cast(TraversalType, data)
