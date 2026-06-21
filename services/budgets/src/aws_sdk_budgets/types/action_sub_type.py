"""Generated from Smithy shape ``com.amazonaws.budgets#ActionSubType``."""

from typing import Literal, TypeAlias, cast

ActionSubType: TypeAlias = Literal[
    "STOP_EC2_INSTANCES",
    "STOP_RDS_INSTANCES",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionSubType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionSubType:
    return cast(ActionSubType, data)
