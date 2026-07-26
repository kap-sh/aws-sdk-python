"""Generated from Smithy shape ``com.amazonaws.licensemanager#ReportFrequencyType``."""

from typing import Literal, TypeAlias, cast

ReportFrequencyType: TypeAlias = Literal[
    "DAY",
    "WEEK",
    "MONTH",
    "ONE_TIME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportFrequencyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReportFrequencyType:
    return cast(ReportFrequencyType, data)
