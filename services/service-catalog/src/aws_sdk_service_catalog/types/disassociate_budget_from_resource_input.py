"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DisassociateBudgetFromResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.budget_name
    import aws_sdk_service_catalog.types.id


class DisassociateBudgetFromResourceInput(TypedDict):
    budget_name: "aws_sdk_service_catalog.types.budget_name.BudgetName"
    """<p>The name of the budget you want to disassociate.</p>"""
    resource_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The resource identifier you want to disassociate from. Either a portfolio-id or a product-id.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateBudgetFromResourceInput) -> dict:
    out: dict = {}
    out["BudgetName"] = value["budget_name"]
    out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateBudgetFromResourceInput:
    out: DisassociateBudgetFromResourceInput = {}  # type: ignore[typeddict-item]
    if "BudgetName" in data:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError(
            "DisassociateBudgetFromResourceInput.budget_name required"
        )
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError(
            "DisassociateBudgetFromResourceInput.resource_id required"
        )
    return out
