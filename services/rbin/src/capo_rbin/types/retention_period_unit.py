"""Generated from Smithy shape ``com.amazonaws.rbin#RetentionPeriodUnit``."""

from typing import Literal, TypeAlias, cast

RetentionPeriodUnit: TypeAlias = Literal["DAYS",]


# --- restJson1 ser/de ---
def serialize_json(value: RetentionPeriodUnit) -> str:
    return value


def deserialize_json(data: str) -> RetentionPeriodUnit:
    return cast(RetentionPeriodUnit, data)
