"""Generated from Smithy shape ``com.amazonaws.servicecatalog#Budgets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.budget_detail

Budgets: TypeAlias = list["capo_service_catalog.types.budget_detail.BudgetDetail"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Budgets) -> list:
    import capo_service_catalog.types.budget_detail

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.budget_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Budgets:
    import capo_service_catalog.types.budget_detail

    out: Budgets = []
    for item in data:
        out.append(
            capo_service_catalog.types.budget_detail.deserialize_aws_json_1_1(item)
        )
    return out
