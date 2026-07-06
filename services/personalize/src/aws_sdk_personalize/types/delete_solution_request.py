"""Generated from Smithy shape ``com.amazonaws.personalize#DeleteSolutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class DeleteSolutionRequest(TypedDict, closed=True):
    solution_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The ARN of the solution to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSolutionRequest) -> dict:
    out: dict = {}
    out["solutionArn"] = value["solution_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSolutionRequest:
    out: DeleteSolutionRequest = {}  # type: ignore[typeddict-item]
    if "solutionArn" in data:
        out["solution_arn"] = data["solutionArn"]
    else:
        raise DeserializationError("DeleteSolutionRequest.solution_arn required")
    return out
