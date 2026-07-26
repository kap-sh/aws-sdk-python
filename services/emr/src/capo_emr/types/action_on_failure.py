"""Generated from Smithy shape ``com.amazonaws.emr#ActionOnFailure``."""

from typing import Literal, TypeAlias, cast

ActionOnFailure: TypeAlias = Literal[
    "TERMINATE_JOB_FLOW",
    "TERMINATE_CLUSTER",
    "CANCEL_AND_WAIT",
    "CONTINUE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionOnFailure) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionOnFailure:
    return cast(ActionOnFailure, data)
