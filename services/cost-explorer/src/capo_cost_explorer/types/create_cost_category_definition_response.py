"""Generated from Smithy shape ``com.amazonaws.costexplorer#CreateCostCategoryDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.arn
    import capo_cost_explorer.types.zoned_date_time


class CreateCostCategoryDefinitionResponse(TypedDict, closed=True):
    cost_category_arn: NotRequired["capo_cost_explorer.types.arn.Arn"]
    """<p>The unique identifier for your newly created cost category. </p>"""
    effective_start: NotRequired[
        "capo_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The cost category's effective start date. It can only be a billing start date (first day of the month).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCostCategoryDefinitionResponse) -> dict:
    out: dict = {}
    if "cost_category_arn" in value:
        out["CostCategoryArn"] = value["cost_category_arn"]
    if "effective_start" in value:
        out["EffectiveStart"] = value["effective_start"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCostCategoryDefinitionResponse:
    out: CreateCostCategoryDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "CostCategoryArn" in data:
        out["cost_category_arn"] = data["CostCategoryArn"]
    if "EffectiveStart" in data:
        out["effective_start"] = data["EffectiveStart"]
    return out
