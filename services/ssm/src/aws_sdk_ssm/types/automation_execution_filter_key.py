"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationExecutionFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_1(value: AutomationExecutionFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutomationExecutionFilterKey:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomationExecutionFilterKey value: {data!r}"
        )
    return cast(AutomationExecutionFilterKey, data)
