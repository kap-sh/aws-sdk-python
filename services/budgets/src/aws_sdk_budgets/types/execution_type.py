"""Generated from Smithy shape ``com.amazonaws.budgets#ExecutionType``."""

from typing import Literal, TypeAlias, cast

ExecutionType: TypeAlias = Literal[
    "APPROVE_BUDGET_ACTION",
    "RETRY_BUDGET_ACTION",
    "REVERSE_BUDGET_ACTION",
    "RESET_BUDGET_ACTION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionType:
    return cast(ExecutionType, data)
