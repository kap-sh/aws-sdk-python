"""Generated from Smithy shape ``com.amazonaws.personalize#CreateSolutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class CreateSolutionResponse(TypedDict, closed=True):
    solution_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The ARN of the solution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSolutionResponse) -> dict:
    out: dict = {}
    if "solution_arn" in value:
        out["solutionArn"] = value["solution_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSolutionResponse:
    out: CreateSolutionResponse = {}  # type: ignore[typeddict-item]
    if "solutionArn" in data:
        out["solution_arn"] = data["solutionArn"]
    return out
