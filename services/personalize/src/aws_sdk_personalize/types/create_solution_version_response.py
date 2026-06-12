"""Generated from Smithy shape ``com.amazonaws.personalize#CreateSolutionVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class CreateSolutionVersionResponse(TypedDict):
    solution_version_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The ARN of the new solution version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSolutionVersionResponse) -> dict:
    out: dict = {}
    if "solution_version_arn" in value:
        out["solutionVersionArn"] = value["solution_version_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSolutionVersionResponse:
    out: CreateSolutionVersionResponse = {}  # type: ignore[typeddict-item]
    if "solutionVersionArn" in data:
        out["solution_version_arn"] = data["solutionVersionArn"]
    return out
