"""Generated from Smithy shape ``com.amazonaws.sagemaker#SchedulerConfigComponent``."""

from typing import Literal, TypeAlias, cast

SchedulerConfigComponent: TypeAlias = Literal[
    "PriorityClasses",
    "FairShare",
    "IdleResourceSharing",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchedulerConfigComponent) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SchedulerConfigComponent:
    return cast(SchedulerConfigComponent, data)
