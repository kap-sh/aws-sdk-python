"""Generated from Smithy shape ``com.amazonaws.ssm#CalendarState``."""

from typing import Literal, TypeAlias, cast

CalendarState: TypeAlias = Literal[
    "OPEN",
    "CLOSED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CalendarState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CalendarState:
    return cast(CalendarState, data)
