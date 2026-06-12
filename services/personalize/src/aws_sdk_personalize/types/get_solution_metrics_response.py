"""Generated from Smithy shape ``com.amazonaws.personalize#GetSolutionMetricsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.metrics


class GetSolutionMetricsResponse(TypedDict):
    solution_version_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The same solution version ARN as specified in the request.</p>"""
    metrics: NotRequired["aws_sdk_personalize.types.metrics.Metrics"]
    """<p>The metrics for the solution version. For more information, see <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/working-with-training-metrics.html\"> Evaluating a solution version with metrics </a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSolutionMetricsResponse) -> dict:
    out: dict = {}
    if "solution_version_arn" in value:
        out["solutionVersionArn"] = value["solution_version_arn"]
    if "metrics" in value:
        import aws_sdk_personalize.types.metrics

        out["metrics"] = aws_sdk_personalize.types.metrics.serialize_aws_json_1_1(
            value["metrics"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSolutionMetricsResponse:
    out: GetSolutionMetricsResponse = {}  # type: ignore[typeddict-item]
    if "solutionVersionArn" in data:
        out["solution_version_arn"] = data["solutionVersionArn"]
    if "metrics" in data:
        import aws_sdk_personalize.types.metrics

        out["metrics"] = aws_sdk_personalize.types.metrics.deserialize_aws_json_1_1(
            data["metrics"]
        )
    return out
