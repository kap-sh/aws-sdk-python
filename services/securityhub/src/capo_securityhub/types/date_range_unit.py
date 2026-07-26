"""Generated from Smithy shape ``com.amazonaws.securityhub#DateRangeUnit``."""

from typing import Literal, TypeAlias, cast

DateRangeUnit: TypeAlias = Literal["DAYS",]


# --- restJson1 ser/de ---
def serialize_json(value: DateRangeUnit) -> str:
    return value


def deserialize_json(data: str) -> DateRangeUnit:
    return cast(DateRangeUnit, data)
