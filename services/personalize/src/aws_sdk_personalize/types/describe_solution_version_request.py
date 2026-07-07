"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeSolutionVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class DescribeSolutionVersionRequest(TypedDict, closed=True):
    solution_version_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the solution version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSolutionVersionRequest) -> dict:
    out: dict = {}
    out["solutionVersionArn"] = value["solution_version_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSolutionVersionRequest:
    out: DescribeSolutionVersionRequest = {}  # type: ignore[typeddict-item]
    if "solutionVersionArn" in data:
        out["solution_version_arn"] = data["solutionVersionArn"]
    else:
        raise DeserializationError(
            "DescribeSolutionVersionRequest.solution_version_arn required"
        )
    return out
