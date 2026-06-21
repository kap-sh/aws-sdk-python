"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryRuleType``."""

from typing import Literal, TypeAlias, cast

CostCategoryRuleType: TypeAlias = Literal[
    "REGULAR",
    "INHERITED_VALUE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategoryRuleType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostCategoryRuleType:
    return cast(CostCategoryRuleType, data)
