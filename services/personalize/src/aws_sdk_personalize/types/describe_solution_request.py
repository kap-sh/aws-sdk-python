"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeSolutionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class DescribeSolutionRequest(TypedDict):
    solution_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the solution to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSolutionRequest) -> dict:
    out: dict = {}
    out["solutionArn"] = value["solution_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSolutionRequest:
    out: DescribeSolutionRequest = {}  # type: ignore[typeddict-item]
    if "solutionArn" in data:
        out["solution_arn"] = data["solutionArn"]
    else:
        raise DeserializationError("DescribeSolutionRequest.solution_arn required")
    return out
