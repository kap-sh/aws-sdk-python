"""Generated from Smithy shape ``com.amazonaws.costexplorer#LookbackPeriodInDays``."""

from typing import Literal, TypeAlias, cast

LookbackPeriodInDays: TypeAlias = Literal[
    "SEVEN_DAYS",
    "THIRTY_DAYS",
    "SIXTY_DAYS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LookbackPeriodInDays) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LookbackPeriodInDays:
    return cast(LookbackPeriodInDays, data)
