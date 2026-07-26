"""Generated from Smithy shape ``com.amazonaws.cloudtrail#RefreshScheduleFrequencyUnit``."""

from typing import Literal, TypeAlias, cast

RefreshScheduleFrequencyUnit: TypeAlias = Literal[
    "HOURS",
    "DAYS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RefreshScheduleFrequencyUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RefreshScheduleFrequencyUnit:
    return cast(RefreshScheduleFrequencyUnit, data)
