"""Generated from Smithy shape ``com.amazonaws.entityresolution#PutPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import capo_entityresolution.types.policy_document
    import capo_entityresolution.types.policy_token
    import capo_entityresolution.types.venice_global_arn


class PutPolicyOutput(TypedDict, closed=True):
    arn: "capo_entityresolution.types.venice_global_arn.VeniceGlobalArn"
    """<p>The Entity Resolution resource ARN.</p>"""
    token: "capo_entityresolution.types.policy_token.PolicyToken"
    """<p>A unique identifier for the current revision of the policy.</p>"""
    policy: NotRequired["capo_entityresolution.types.policy_document.PolicyDocument"]
    """<p>The resource-based policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutPolicyOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["token"] = value["token"]
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutPolicyOutput:
    out: PutPolicyOutput = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("PutPolicyOutput.arn required")
    if "token" in data:
        out["token"] = data["token"]
    else:
        raise DeserializationError("PutPolicyOutput.token required")
    if "policy" in data:
        out["policy"] = data["policy"]
    return out
