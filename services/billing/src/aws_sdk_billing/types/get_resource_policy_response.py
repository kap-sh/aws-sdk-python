"""Generated from Smithy shape ``com.amazonaws.billing#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_billing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billing.types.policy_document
    import aws_sdk_billing.types.resource_arn


class GetResourcePolicyResponse(TypedDict):
    resource_arn: "aws_sdk_billing.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the billing view resource to which the policy is attached to. </p>"""
    policy: NotRequired["aws_sdk_billing.types.policy_document.PolicyDocument"]
    """<p>The resource-based policy document attached to the resource in <code>JSON</code> format. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("GetResourcePolicyResponse.resource_arn required")
    if "policy" in data:
        out["policy"] = data["policy"]
    return out
