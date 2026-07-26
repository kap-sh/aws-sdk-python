"""Generated from Smithy shape ``com.amazonaws.dlm#RetentionIntervalUnitValues``."""

from typing import Literal, TypeAlias, cast

RetentionIntervalUnitValues: TypeAlias = Literal[
    "DAYS",
    "WEEKS",
    "MONTHS",
    "YEARS",
]


# --- restJson1 ser/de ---
def serialize_json(value: RetentionIntervalUnitValues) -> str:
    return value


def deserialize_json(data: str) -> RetentionIntervalUnitValues:
    return cast(RetentionIntervalUnitValues, data)
