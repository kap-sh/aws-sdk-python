"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeAlgorithmRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class DescribeAlgorithmRequest(TypedDict):
    algorithm_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the algorithm to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAlgorithmRequest) -> dict:
    out: dict = {}
    out["algorithmArn"] = value["algorithm_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAlgorithmRequest:
    out: DescribeAlgorithmRequest = {}  # type: ignore[typeddict-item]
    if "algorithmArn" in data:
        out["algorithm_arn"] = data["algorithmArn"]
    else:
        raise DeserializationError("DescribeAlgorithmRequest.algorithm_arn required")
    return out
