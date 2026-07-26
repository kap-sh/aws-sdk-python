"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RangeUnit``."""

from typing import Literal, TypeAlias, cast

RangeUnit: TypeAlias = Literal["DAYS",]


# --- restJson1 ser/de ---
def serialize_json(value: RangeUnit) -> str:
    return value


def deserialize_json(data: str) -> RangeUnit:
    return cast(RangeUnit, data)
