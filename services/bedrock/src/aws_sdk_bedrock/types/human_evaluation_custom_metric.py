"""Generated from Smithy shape ``com.amazonaws.bedrock#HumanEvaluationCustomMetric``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_metric_description
    import aws_sdk_bedrock.types.evaluation_metric_name
    import aws_sdk_bedrock.types.evaluation_rating_method


class HumanEvaluationCustomMetric(TypedDict):
    name: "aws_sdk_bedrock.types.evaluation_metric_name.EvaluationMetricName"
    """<p>The name of the metric. Your human evaluators will see this name in the evaluation UI.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock.types.evaluation_metric_description.EvaluationMetricDescription"
    ]
    """<p>An optional description of the metric. Use this parameter to provide more details about the metric.</p>"""
    rating_method: (
        "aws_sdk_bedrock.types.evaluation_rating_method.EvaluationRatingMethod"
    )
    """<p>Choose how you want your human workers to evaluation your model. Valid values for rating methods are <code>ThumbsUpDown</code>, <code>IndividualLikertScale</code>,<code>ComparisonLikertScale</code>, <code>ComparisonChoice</code>, and <code>ComparisonRank</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HumanEvaluationCustomMetric) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["ratingMethod"] = value["rating_method"]
    return out


def deserialize_json(data: dict) -> HumanEvaluationCustomMetric:
    out: HumanEvaluationCustomMetric = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("HumanEvaluationCustomMetric.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "ratingMethod" in data:
        out["rating_method"] = data["ratingMethod"]
    else:
        raise DeserializationError("HumanEvaluationCustomMetric.rating_method required")
    return out
