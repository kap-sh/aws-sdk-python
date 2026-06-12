"""Generated from Smithy shape ``com.amazonaws.budgets#ExecutionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_budgets.errors import DeserializationError

ExecutionType: TypeAlias = Literal[
    "APPROVE_BUDGET_ACTION",
    "RETRY_BUDGET_ACTION",
    "REVERSE_BUDGET_ACTION",
    "RESET_BUDGET_ACTION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPROVE_BUDGET_ACTION",
        "RETRY_BUDGET_ACTION",
        "REVERSE_BUDGET_ACTION",
        "RESET_BUDGET_ACTION",
    )
)


def serialize_aws_json_1_1(value: ExecutionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionType value: {data!r}")
    return cast(ExecutionType, data)
