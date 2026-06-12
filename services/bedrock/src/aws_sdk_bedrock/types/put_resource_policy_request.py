"""Generated from Smithy shape ``com.amazonaws.bedrock#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.resource_policy_document
    import aws_sdk_bedrock.types.resource_policy_resource_arn


class PutResourcePolicyRequest(TypedDict):
    resource_arn: (
        "aws_sdk_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn"
    )
    """<p>The ARN of the Bedrock resource to which this resource policy applies.</p>"""
    resource_policy: (
        "aws_sdk_bedrock.types.resource_policy_document.ResourcePolicyDocument"
    )
    """<p>The JSON string representing the Bedrock resource policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["resourcePolicy"] = value["resource_policy"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.resource_arn required")
    if "resourcePolicy" in data:
        out["resource_policy"] = data["resourcePolicy"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.resource_policy required")
    return out
