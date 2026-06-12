"""Generated from Smithy shape ``com.amazonaws.servicecatalog#Budgets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.budget_detail

Budgets: TypeAlias = list["aws_sdk_service_catalog.types.budget_detail.BudgetDetail"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Budgets) -> list:
    import aws_sdk_service_catalog.types.budget_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.budget_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Budgets:
    import aws_sdk_service_catalog.types.budget_detail

    out: Budgets = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.budget_detail.deserialize_aws_json_1_1(item)
        )
    return out
