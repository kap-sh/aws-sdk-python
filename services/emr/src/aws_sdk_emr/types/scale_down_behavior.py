"""Generated from Smithy shape ``com.amazonaws.emr#ScaleDownBehavior``."""

from typing import Literal, TypeAlias, cast

ScaleDownBehavior: TypeAlias = Literal[
    "TERMINATE_AT_INSTANCE_HOUR",
    "TERMINATE_AT_TASK_COMPLETION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScaleDownBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScaleDownBehavior:
    return cast(ScaleDownBehavior, data)
