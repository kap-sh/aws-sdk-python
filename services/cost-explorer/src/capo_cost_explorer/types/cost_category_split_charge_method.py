"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategorySplitChargeMethod``."""

from typing import Literal, TypeAlias, cast

CostCategorySplitChargeMethod: TypeAlias = Literal[
    "FIXED",
    "PROPORTIONAL",
    "EVEN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategorySplitChargeMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostCategorySplitChargeMethod:
    return cast(CostCategorySplitChargeMethod, data)
