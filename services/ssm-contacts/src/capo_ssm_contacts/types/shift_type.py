"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ShiftType``."""

from typing import Literal, TypeAlias, cast

ShiftType: TypeAlias = Literal[
    "REGULAR",
    "OVERRIDDEN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShiftType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ShiftType:
    return cast(ShiftType, data)
