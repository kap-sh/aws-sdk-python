"""Generated from Smithy shape ``com.amazonaws.savingsplans#SavingsPlanProductTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plan_product_type

SavingsPlanProductTypeList: TypeAlias = list[
    "capo_savingsplans.types.savings_plan_product_type.SavingsPlanProductType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SavingsPlanProductTypeList) -> list:
    import capo_savingsplans.types.savings_plan_product_type

    out: list = []
    for item in value:
        out.append(
            capo_savingsplans.types.savings_plan_product_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SavingsPlanProductTypeList:
    import capo_savingsplans.types.savings_plan_product_type

    out: SavingsPlanProductTypeList = []
    for item in data:
        out.append(
            capo_savingsplans.types.savings_plan_product_type.deserialize_json(item)
        )
    return out
