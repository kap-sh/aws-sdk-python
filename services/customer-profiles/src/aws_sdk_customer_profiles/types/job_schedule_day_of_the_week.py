"""Generated from Smithy shape ``com.amazonaws.customerprofiles#JobScheduleDayOfTheWeek``."""

from typing import Literal, TypeAlias, cast

JobScheduleDayOfTheWeek: TypeAlias = Literal[
    "SUNDAY",
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobScheduleDayOfTheWeek) -> str:
    return value


def deserialize_json(data: str) -> JobScheduleDayOfTheWeek:
    return cast(JobScheduleDayOfTheWeek, data)
