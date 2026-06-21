"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategorySplitChargeRuleParameterType``."""

from typing import Literal, TypeAlias, cast

CostCategorySplitChargeRuleParameterType: TypeAlias = Literal["ALLOCATION_PERCENTAGES",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategorySplitChargeRuleParameterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostCategorySplitChargeRuleParameterType:
    return cast(CostCategorySplitChargeRuleParameterType, data)
