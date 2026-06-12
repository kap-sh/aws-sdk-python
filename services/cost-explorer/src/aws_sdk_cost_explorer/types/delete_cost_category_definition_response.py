"""Generated from Smithy shape ``com.amazonaws.costexplorer#DeleteCostCategoryDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.arn
    import aws_sdk_cost_explorer.types.zoned_date_time


class DeleteCostCategoryDefinitionResponse(TypedDict):
    cost_category_arn: NotRequired["aws_sdk_cost_explorer.types.arn.Arn"]
    """<p>The unique identifier for your cost category. </p>"""
    effective_end: NotRequired[
        "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The effective end date of the cost category as a result of deleting it. No costs after this date is categorized by the deleted cost category. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCostCategoryDefinitionResponse) -> dict:
    out: dict = {}
    if "cost_category_arn" in value:
        out["CostCategoryArn"] = value["cost_category_arn"]
    if "effective_end" in value:
        out["EffectiveEnd"] = value["effective_end"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCostCategoryDefinitionResponse:
    out: DeleteCostCategoryDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "CostCategoryArn" in data:
        out["cost_category_arn"] = data["CostCategoryArn"]
    if "EffectiveEnd" in data:
        out["effective_end"] = data["EffectiveEnd"]
    return out
