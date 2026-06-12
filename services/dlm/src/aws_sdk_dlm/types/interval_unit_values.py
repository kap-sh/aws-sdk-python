"""Generated from Smithy shape ``com.amazonaws.dlm#IntervalUnitValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dlm.errors import DeserializationError

IntervalUnitValues: TypeAlias = Literal["HOURS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("HOURS",))


def serialize_json(value: IntervalUnitValues) -> str:
    return value


def deserialize_json(data: str) -> IntervalUnitValues:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IntervalUnitValues value: {data!r}")
    return cast(IntervalUnitValues, data)
