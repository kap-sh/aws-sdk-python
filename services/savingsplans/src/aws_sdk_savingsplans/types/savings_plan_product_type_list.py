"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanProductTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.savings_plan_product_type

SavingsPlanProductTypeList: TypeAlias = list[
    "aws_sdk_savingsplans.types.savings_plan_product_type.SavingsPlanProductType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanProductTypeList) -> list:
    import aws_sdk_savingsplans.types.savings_plan_product_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_savingsplans.types.savings_plan_product_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SavingsPlanProductTypeList:
    import aws_sdk_savingsplans.types.savings_plan_product_type

    out: SavingsPlanProductTypeList = []
    for item in data:
        out.append(
            aws_sdk_savingsplans.types.savings_plan_product_type.deserialize_json(item)
        )
    return out
