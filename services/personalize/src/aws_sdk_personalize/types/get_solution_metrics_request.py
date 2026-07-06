"""Generated from Smithy shape ``com.amazonaws.personalize#GetSolutionMetricsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class GetSolutionMetricsRequest(TypedDict, closed=True):
    solution_version_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the solution version for which to get metrics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSolutionMetricsRequest) -> dict:
    out: dict = {}
    out["solutionVersionArn"] = value["solution_version_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSolutionMetricsRequest:
    out: GetSolutionMetricsRequest = {}  # type: ignore[typeddict-item]
    if "solutionVersionArn" in data:
        out["solution_version_arn"] = data["solutionVersionArn"]
    else:
        raise DeserializationError(
            "GetSolutionMetricsRequest.solution_version_arn required"
        )
    return out
