"""Generated from Smithy shape ``com.amazonaws.ecs#SettingName``."""

from typing import Literal, TypeAlias, cast

SettingName: TypeAlias = Literal[
    "serviceLongArnFormat",
    "taskLongArnFormat",
    "containerInstanceLongArnFormat",
    "awsvpcTrunking",
    "containerInsights",
    "fargateFIPSMode",
    "tagResourceAuthorization",
    "fargateTaskRetirementWaitPeriod",
    "guardDutyActivate",
    "defaultLogDriverMode",
    "fargateEventWindows",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SettingName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SettingName:
    return cast(SettingName, data)
