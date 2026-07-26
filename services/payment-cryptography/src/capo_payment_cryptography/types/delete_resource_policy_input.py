"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#DeleteResourcePolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.resource_arn


class DeleteResourcePolicyInput(TypedDict, closed=True):
    resource_arn: "capo_payment_cryptography.types.resource_arn.ResourceArn"
    """<p>The <code>KeyARN</code> of the key whose resource-based policy you want to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteResourcePolicyInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteResourcePolicyInput:
    out: DeleteResourcePolicyInput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("DeleteResourcePolicyInput.resource_arn required")
    return out
