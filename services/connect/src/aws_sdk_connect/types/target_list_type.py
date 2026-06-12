"""Generated from Smithy shape ``com.amazonaws.connect#TargetListType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

TargetListType: TypeAlias = Literal["PROFICIENCIES",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PROFICIENCIES",))


def serialize_json(value: TargetListType) -> str:
    return value


def deserialize_json(data: str) -> TargetListType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetListType value: {data!r}")
    return cast(TargetListType, data)
