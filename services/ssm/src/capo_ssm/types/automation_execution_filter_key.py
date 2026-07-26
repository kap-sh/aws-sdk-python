"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationExecutionFilterKey``."""

from typing import Literal, TypeAlias, cast

AutomationExecutionFilterKey: TypeAlias = Literal[
    "DocumentNamePrefix",
    "ExecutionStatus",
    "ExecutionId",
    "ParentExecutionId",
    "CurrentAction",
    "StartTimeBefore",
    "StartTimeAfter",
    "AutomationType",
    "TagKey",
    "TargetResourceGroup",
    "AutomationSubtype",
    "OpsItemId",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomationExecutionFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutomationExecutionFilterKey:
    return cast(AutomationExecutionFilterKey, data)
