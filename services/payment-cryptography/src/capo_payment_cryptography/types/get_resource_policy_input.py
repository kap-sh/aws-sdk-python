"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#GetResourcePolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.resource_arn


class GetResourcePolicyInput(TypedDict, closed=True):
    resource_arn: "capo_payment_cryptography.types.resource_arn.ResourceArn"
    """<p>The <code>KeyARN</code> of the key whose resource-based policy you want to retrieve.</p>"""


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
