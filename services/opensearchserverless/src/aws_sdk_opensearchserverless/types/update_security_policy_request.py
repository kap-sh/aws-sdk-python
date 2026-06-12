"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateSecurityPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.client_token
    import aws_sdk_opensearchserverless.types.policy_description
    import aws_sdk_opensearchserverless.types.policy_document
    import aws_sdk_opensearchserverless.types.policy_name
    import aws_sdk_opensearchserverless.types.policy_version
    import aws_sdk_opensearchserverless.types.security_policy_type


class UpdateSecurityPolicyRequest(TypedDict):
    type: "aws_sdk_opensearchserverless.types.security_policy_type.SecurityPolicyType"
    """<p>The type of access policy.</p>"""
    name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName"
    """<p>The name of the policy.</p>"""
    policy_version: "aws_sdk_opensearchserverless.types.policy_version.PolicyVersion"
    """<p>The version of the policy being updated.</p>"""
    description: NotRequired[
        "aws_sdk_opensearchserverless.types.policy_description.PolicyDescription"
    ]
    """<p>A description of the policy. Typically used to store information about the permissions defined in the policy.</p>"""
    policy: NotRequired[
        "aws_sdk_opensearchserverless.types.policy_document.PolicyDocument"
    ]
    """<p>The JSON policy document to use as the content for the new policy.</p>"""
    client_token: NotRequired[
        "aws_sdk_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateSecurityPolicyRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["name"] = value["name"]
    out["policyVersion"] = value["policy_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "policy" in value:
        out["policy"] = value["policy"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateSecurityPolicyRequest:
    out: UpdateSecurityPolicyRequest = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("UpdateSecurityPolicyRequest.type required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateSecurityPolicyRequest.name required")
    if "policyVersion" in data:
        out["policy_version"] = data["policyVersion"]
    else:
        raise DeserializationError(
            "UpdateSecurityPolicyRequest.policy_version required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "policy" in data:
        out["policy"] = data["policy"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
