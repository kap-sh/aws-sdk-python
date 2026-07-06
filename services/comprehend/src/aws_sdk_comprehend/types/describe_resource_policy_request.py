"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.comprehend_model_arn


class DescribeResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    """<p>The Amazon Resource Name (ARN) of the custom model version that has the resource policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeResourcePolicyRequest:
    out: DescribeResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "DescribeResourcePolicyRequest.resource_arn required"
        )
    return out
