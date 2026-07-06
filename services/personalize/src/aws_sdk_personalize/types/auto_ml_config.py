"""Generated from Smithy shape ``com.amazonaws.personalize#AutoMLConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn_list
    import aws_sdk_personalize.types.metric_name


class AutoMLConfig(TypedDict, closed=True):
    metric_name: NotRequired["aws_sdk_personalize.types.metric_name.MetricName"]
    """<p>The metric to optimize.</p>"""
    recipe_list: NotRequired["aws_sdk_personalize.types.arn_list.ArnList"]
    """<p>The list of candidate recipes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLConfig) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["metricName"] = value["metric_name"]
    if "recipe_list" in value:
        import aws_sdk_personalize.types.arn_list

        out["recipeList"] = aws_sdk_personalize.types.arn_list.serialize_aws_json_1_1(
            value["recipe_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLConfig:
    out: AutoMLConfig = {}  # type: ignore[typeddict-item]
    if "metricName" in data:
        out["metric_name"] = data["metricName"]
    if "recipeList" in data:
        import aws_sdk_personalize.types.arn_list

        out["recipe_list"] = (
            aws_sdk_personalize.types.arn_list.deserialize_aws_json_1_1(
                data["recipeList"]
            )
        )
    return out
