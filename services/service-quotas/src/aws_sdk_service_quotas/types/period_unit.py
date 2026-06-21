"""Generated from Smithy shape ``com.amazonaws.servicequotas#PeriodUnit``."""

from typing import Literal, TypeAlias, cast

PeriodUnit: TypeAlias = Literal[
    "MICROSECOND",
    "MILLISECOND",
    "SECOND",
    "MINUTE",
    "HOUR",
    "DAY",
    "WEEK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PeriodUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PeriodUnit:
    return cast(PeriodUnit, data)
