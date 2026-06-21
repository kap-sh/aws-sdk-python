"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#DayOfWeek``."""

from typing import Literal, TypeAlias, cast

DayOfWeek: TypeAlias = Literal[
    "MON",
    "TUE",
    "WED",
    "THU",
    "FRI",
    "SAT",
    "SUN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DayOfWeek) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DayOfWeek:
    return cast(DayOfWeek, data)
