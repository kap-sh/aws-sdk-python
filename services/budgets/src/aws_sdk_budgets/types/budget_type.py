"""Generated from Smithy shape ``com.amazonaws.budgets#BudgetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_budgets.errors import DeserializationError

"""<p> The type of a budget. It must be one of the following types: </p> <p> <code>COST</code>, <code>USAGE</code>, <code>RI_UTILIZATION</code>, <code>RI_COVERAGE</code>, <code>SAVINGS_PLANS_UTILIZATION</code>, or <code>SAVINGS_PLANS_COVERAGE</code>.</p>"""
BudgetType: TypeAlias = Literal[
    "USAGE",
    "COST",
    "RI_UTILIZATION",
    "RI_COVERAGE",
    "SAVINGS_PLANS_UTILIZATION",
    "SAVINGS_PLANS_COVERAGE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USAGE",
        "COST",
        "RI_UTILIZATION",
        "RI_COVERAGE",
        "SAVINGS_PLANS_UTILIZATION",
        "SAVINGS_PLANS_COVERAGE",
    )
)


def serialize_aws_json_1_1(value: BudgetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BudgetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BudgetType value: {data!r}")
    return cast(BudgetType, data)
