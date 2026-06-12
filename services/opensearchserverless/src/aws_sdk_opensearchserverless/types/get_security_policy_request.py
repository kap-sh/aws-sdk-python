"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#GetSecurityPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.policy_name
    import aws_sdk_opensearchserverless.types.security_policy_type


class GetSecurityPolicyRequest(TypedDict):
    type: "aws_sdk_opensearchserverless.types.security_policy_type.SecurityPolicyType"
    """<p>The type of security policy.</p>"""
    name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName"
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
