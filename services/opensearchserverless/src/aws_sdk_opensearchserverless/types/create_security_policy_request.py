"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateSecurityPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.client_token
    import aws_sdk_opensearchserverless.types.policy_description
    import aws_sdk_opensearchserverless.types.policy_document
    import aws_sdk_opensearchserverless.types.policy_name
    import aws_sdk_opensearchserverless.types.security_policy_type


class CreateSecurityPolicyRequest(TypedDict, closed=True):
    type: "aws_sdk_opensearchserverless.types.security_policy_type.SecurityPolicyType"
    """<p>The type of security policy.</p>"""
    name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName"
    """<p>The name of the policy.</p>"""
    description: NotRequired[
        "aws_sdk_opensearchserverless.types.policy_description.PolicyDescription"
    ]
    """<p>A description of the policy. Typically used to store information about the permissions defined in the policy.</p>"""
    policy: "aws_sdk_opensearchserverless.types.policy_document.PolicyDocument"
    """<p>The JSON policy document to use as the content for the new policy.</p>"""
    client_token: NotRequired[
        "aws_sdk_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateSecurityPolicyRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["policy"] = value["policy"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateSecurityPolicyRequest:
    out: CreateSecurityPolicyRequest = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CreateSecurityPolicyRequest.type required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateSecurityPolicyRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "policy" in data:
        out["policy"] = data["policy"]
    else:
        raise DeserializationError("CreateSecurityPolicyRequest.policy required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
