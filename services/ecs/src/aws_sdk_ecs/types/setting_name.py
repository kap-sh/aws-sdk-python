"""Generated from Smithy shape ``com.amazonaws.ecs#SettingName``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_1(value: SettingName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SettingName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SettingName value: {data!r}")
    return cast(SettingName, data)
