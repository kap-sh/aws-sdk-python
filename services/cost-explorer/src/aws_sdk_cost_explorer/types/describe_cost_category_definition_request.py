"""Generated from Smithy shape ``com.amazonaws.costexplorer#DescribeCostCategoryDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.arn
    import aws_sdk_cost_explorer.types.zoned_date_time


class DescribeCostCategoryDefinitionRequest(TypedDict):
    cost_category_arn: "aws_sdk_cost_explorer.types.arn.Arn"
    """<p>The unique identifier for your cost category. </p>"""
    effective_on: NotRequired[
        "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The date when the cost category was effective. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCostCategoryDefinitionRequest) -> dict:
    out: dict = {}
    out["CostCategoryArn"] = value["cost_category_arn"]
    if "effective_on" in value:
        out["EffectiveOn"] = value["effective_on"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCostCategoryDefinitionRequest:
    out: DescribeCostCategoryDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "CostCategoryArn" in data:
        out["cost_category_arn"] = data["CostCategoryArn"]
    else:
        raise DeserializationError(
            "DescribeCostCategoryDefinitionRequest.cost_category_arn required"
        )
    if "EffectiveOn" in data:
        out["effective_on"] = data["EffectiveOn"]
    return out
