"""Generated from Smithy shape ``com.amazonaws.entityresolution#PutPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.policy_document
    import aws_sdk_entityresolution.types.policy_token
    import aws_sdk_entityresolution.types.venice_global_arn


class PutPolicyInput(TypedDict, closed=True):
    arn: "aws_sdk_entityresolution.types.venice_global_arn.VeniceGlobalArn"
    """<p>The Amazon Resource Name (ARN) of the resource for which the policy needs to be updated.</p>"""
    token: NotRequired["aws_sdk_entityresolution.types.policy_token.PolicyToken"]
    """<p>A unique identifier for the current revision of the policy.</p>"""
    policy: "aws_sdk_entityresolution.types.policy_document.PolicyDocument"
    """<p>The resource-based policy.</p> <important> <p>If you set the value of the <code>effect</code> parameter in the <code>policy</code> to <code>Deny</code> for the <code>PutPolicy</code> operation, you must also set the value of the <code>effect</code> parameter to <code>Deny</code> for the <code>AddPolicyStatement</code> operation.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutPolicyInput) -> dict:
    out: dict = {}
    if "token" in value:
        out["token"] = value["token"]
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutPolicyInput:
    out: PutPolicyInput = {}  # type: ignore[typeddict-item]
    if "token" in data:
        out["token"] = data["token"]
    if "policy" in data:
        out["policy"] = data["policy"]
    else:
        raise DeserializationError("PutPolicyInput.policy required")
    return out
