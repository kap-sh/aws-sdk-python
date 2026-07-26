"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#GetResourcePolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.resource_arn
    import capo_payment_cryptography.types.resource_policy


class GetResourcePolicyOutput(TypedDict, closed=True):
    resource_arn: "capo_payment_cryptography.types.resource_arn.ResourceArn"
    """<p>The <code>KeyARN</code> of the key.</p>"""
    policy: "capo_payment_cryptography.types.resource_policy.ResourcePolicy"
    """<p>The resource-based policy attached to the key, in JSON format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourcePolicyOutput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourcePolicyOutput:
    out: GetResourcePolicyOutput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("GetResourcePolicyOutput.resource_arn required")
    if "Policy" in data:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("GetResourcePolicyOutput.policy required")
    return out
