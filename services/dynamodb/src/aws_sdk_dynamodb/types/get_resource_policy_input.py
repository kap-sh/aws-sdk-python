"""Generated from Smithy shape ``com.amazonaws.dynamodb#GetResourcePolicyInput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.resource_arn_string


class GetResourcePolicyInput(TypedDict):
    resource_arn: "aws_sdk_dynamodb.types.resource_arn_string.ResourceArnString"
    """<p>The Amazon Resource Name (ARN) of the DynamoDB resource to which the policy is attached. The resources you can specify include tables and streams.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourcePolicyInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourcePolicyInput:
    out: GetResourcePolicyInput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("GetResourcePolicyInput.resource_arn required")
    return out
