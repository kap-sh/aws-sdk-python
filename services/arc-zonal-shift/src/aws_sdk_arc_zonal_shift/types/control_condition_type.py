"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ControlConditionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_zonal_shift.errors import DeserializationError

ControlConditionType: TypeAlias = Literal["CLOUDWATCH",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CLOUDWATCH",))


def serialize_json(value: ControlConditionType) -> str:
    return value


def deserialize_json(data: str) -> ControlConditionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ControlConditionType value: {data!r}")
    return cast(ControlConditionType, data)
