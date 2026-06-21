"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryStatusComponent``."""

from typing import Literal, TypeAlias, cast

CostCategoryStatusComponent: TypeAlias = Literal["COST_EXPLORER",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategoryStatusComponent) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostCategoryStatusComponent:
    return cast(CostCategoryStatusComponent, data)
