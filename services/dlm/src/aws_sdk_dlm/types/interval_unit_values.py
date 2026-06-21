"""Generated from Smithy shape ``com.amazonaws.dlm#IntervalUnitValues``."""

from typing import Literal, TypeAlias, cast

IntervalUnitValues: TypeAlias = Literal["HOURS",]


# --- restJson1 ser/de ---
def serialize_json(value: IntervalUnitValues) -> str:
    return value


def deserialize_json(data: str) -> IntervalUnitValues:
    return cast(IntervalUnitValues, data)
