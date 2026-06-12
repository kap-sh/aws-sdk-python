"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryResourceAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.arn
    import aws_sdk_cost_explorer.types.cost_category_name
    import aws_sdk_cost_explorer.types.generic_arn


class CostCategoryResourceAssociation(TypedDict):
    resource_arn: NotRequired["aws_sdk_cost_explorer.types.generic_arn.GenericArn"]
    """<p> The unique identifier for an associated resource. </p>"""
    cost_category_name: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_name.CostCategoryName"
    ]
    cost_category_arn: NotRequired["aws_sdk_cost_explorer.types.arn.Arn"]
    """<p>The unique identifier for your cost category. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategoryResourceAssociation) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "cost_category_name" in value:
        out["CostCategoryName"] = value["cost_category_name"]
    if "cost_category_arn" in value:
        out["CostCategoryArn"] = value["cost_category_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CostCategoryResourceAssociation:
    out: CostCategoryResourceAssociation = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "CostCategoryName" in data:
        out["cost_category_name"] = data["CostCategoryName"]
    if "CostCategoryArn" in data:
        out["cost_category_arn"] = data["CostCategoryArn"]
    return out
