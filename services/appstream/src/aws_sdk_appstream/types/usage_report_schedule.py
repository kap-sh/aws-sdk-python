"""Generated from Smithy shape ``com.amazonaws.appstream#UsageReportSchedule``."""

from typing import Literal, TypeAlias, cast

UsageReportSchedule: TypeAlias = Literal["DAILY",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageReportSchedule) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UsageReportSchedule:
    return cast(UsageReportSchedule, data)
