"""Generated from Smithy shape ``com.amazonaws.billing#GetResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_billing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billing.types.resource_arn


class GetResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_billing.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the billing view resource to which the policy is attached to. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourcePolicyRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourcePolicyRequest:
    out: GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("GetResourcePolicyRequest.resource_arn required")
    return out
