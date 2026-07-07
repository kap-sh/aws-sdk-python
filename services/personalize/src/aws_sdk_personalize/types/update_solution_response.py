"""Generated from Smithy shape ``com.amazonaws.personalize#UpdateSolutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class UpdateSolutionResponse(TypedDict, closed=True):
    solution_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The same solution Amazon Resource Name (ARN) as given in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSolutionResponse) -> dict:
    out: dict = {}
    if "solution_arn" in value:
        out["solutionArn"] = value["solution_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSolutionResponse:
    out: UpdateSolutionResponse = {}  # type: ignore[typeddict-item]
    if "solutionArn" in data:
        out["solution_arn"] = data["solutionArn"]
    return out
