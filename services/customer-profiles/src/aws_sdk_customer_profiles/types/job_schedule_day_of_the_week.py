"""Generated from Smithy shape ``com.amazonaws.customerprofiles#JobScheduleDayOfTheWeek``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "SUNDAY",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
    )
)


def serialize_json(value: JobScheduleDayOfTheWeek) -> str:
    return value


def deserialize_json(data: str) -> JobScheduleDayOfTheWeek:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobScheduleDayOfTheWeek value: {data!r}")
    return cast(JobScheduleDayOfTheWeek, data)
