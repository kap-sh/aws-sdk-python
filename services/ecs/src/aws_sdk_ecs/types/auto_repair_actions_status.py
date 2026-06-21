"""Generated from Smithy shape ``com.amazonaws.ecs#AutoRepairActionsStatus``."""

from typing import Literal, TypeAlias, cast

AutoRepairActionsStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoRepairActionsStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoRepairActionsStatus:
    return cast(AutoRepairActionsStatus, data)
