"""Generated from Smithy shape ``com.amazonaws.inspector2#TagComparison``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

TagComparison: TypeAlias = Literal["EQUALS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EQUALS",))


def serialize_json(value: TagComparison) -> str:
    return value


def deserialize_json(data: str) -> TagComparison:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TagComparison value: {data!r}")
    return cast(TagComparison, data)
