"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryRuleVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

"""<p>The rule schema version in this particular cost category.</p>"""
CostCategoryRuleVersion: TypeAlias = Literal["CostCategoryExpression.v1",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CostCategoryExpression.v1",))


def serialize_aws_json_1_1(value: CostCategoryRuleVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostCategoryRuleVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CostCategoryRuleVersion value: {data!r}")
    return cast(CostCategoryRuleVersion, data)
