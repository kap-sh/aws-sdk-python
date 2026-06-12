"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#PutResourcePolicyOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.resource_arn
    import aws_sdk_payment_cryptography.types.resource_policy


class PutResourcePolicyOutput(TypedDict):
    resource_arn: "aws_sdk_payment_cryptography.types.resource_arn.ResourceArn"
    """<p>The <code>KeyARN</code> of the key that the resource-based policy was attached to.</p>"""
    policy: "aws_sdk_payment_cryptography.types.resource_policy.ResourcePolicy"
    """<p>The resource-based policy that was attached to the key.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutResourcePolicyOutput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutResourcePolicyOutput:
    out: PutResourcePolicyOutput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("PutResourcePolicyOutput.resource_arn required")
    if "Policy" in data:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("PutResourcePolicyOutput.policy required")
    return out
