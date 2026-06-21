"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#TimeUnitsType``."""

from typing import Literal, TypeAlias, cast

TimeUnitsType: TypeAlias = Literal[
    "seconds",
    "minutes",
    "hours",
    "days",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeUnitsType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TimeUnitsType:
    return cast(TimeUnitsType, data)
