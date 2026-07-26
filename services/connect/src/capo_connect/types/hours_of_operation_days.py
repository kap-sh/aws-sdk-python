"""Generated from Smithy shape ``com.amazonaws.connect#HoursOfOperationDays``."""

from typing import Literal, TypeAlias, cast

HoursOfOperationDays: TypeAlias = Literal[
    "SUNDAY",
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
]


# --- restJson1 ser/de ---
def serialize_json(value: HoursOfOperationDays) -> str:
    return value


def deserialize_json(data: str) -> HoursOfOperationDays:
    return cast(HoursOfOperationDays, data)
