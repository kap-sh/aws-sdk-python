"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryRuleVersion``."""

from typing import Literal, TypeAlias, cast

"""<p>The rule schema version in this particular cost category.</p>"""
CostCategoryRuleVersion: TypeAlias = Literal["CostCategoryExpression.v1",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategoryRuleVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostCategoryRuleVersion:
    return cast(CostCategoryRuleVersion, data)
