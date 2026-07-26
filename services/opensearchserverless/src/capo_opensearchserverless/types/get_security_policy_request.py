"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#GetSecurityPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearchserverless.types.policy_name
    import capo_opensearchserverless.types.security_policy_type


class GetSecurityPolicyRequest(TypedDict, closed=True):
    type: "capo_opensearchserverless.types.security_policy_type.SecurityPolicyType"
    """<p>The type of security policy.</p>"""
    name: "capo_opensearchserverless.types.policy_name.PolicyName"
    """<p>The name of the security policy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetSecurityPolicyRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetSecurityPolicyRequest:
    out: GetSecurityPolicyRequest = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("GetSecurityPolicyRequest.type required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetSecurityPolicyRequest.name required")
    return out
