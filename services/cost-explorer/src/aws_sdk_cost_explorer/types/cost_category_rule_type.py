"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryRuleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

CostCategoryRuleType: TypeAlias = Literal[
    "REGULAR",
    "INHERITED_VALUE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGULAR",
        "INHERITED_VALUE",
    )
)


def serialize_aws_json_1_1(value: CostCategoryRuleType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostCategoryRuleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CostCategoryRuleType value: {data!r}")
    return cast(CostCategoryRuleType, data)
