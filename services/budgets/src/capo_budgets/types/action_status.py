"""Generated from Smithy shape ``com.amazonaws.budgets#ActionStatus``."""

from typing import Literal, TypeAlias, cast

ActionStatus: TypeAlias = Literal[
    "STANDBY",
    "PENDING",
    "EXECUTION_IN_PROGRESS",
    "EXECUTION_SUCCESS",
    "EXECUTION_FAILURE",
    "REVERSE_IN_PROGRESS",
    "REVERSE_SUCCESS",
    "REVERSE_FAILURE",
    "RESET_IN_PROGRESS",
    "RESET_FAILURE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionStatus:
    return cast(ActionStatus, data)
