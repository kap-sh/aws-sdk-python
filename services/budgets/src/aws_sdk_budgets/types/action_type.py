"""Generated from Smithy shape ``com.amazonaws.budgets#ActionType``."""

from typing import Literal, TypeAlias, cast

ActionType: TypeAlias = Literal[
    "APPLY_IAM_POLICY",
    "APPLY_SCP_POLICY",
    "RUN_SSM_DOCUMENTS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionType:
    return cast(ActionType, data)
