"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateLifecyclePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.lifecycle_policy_type
    import capo_opensearchserverless.types.policy_description
    import capo_opensearchserverless.types.policy_document
    import capo_opensearchserverless.types.policy_name
    import capo_opensearchserverless.types.policy_version


class UpdateLifecyclePolicyRequest(TypedDict, closed=True):
    type: "capo_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType"
    """<p> The type of lifecycle policy.</p>"""
    name: "capo_opensearchserverless.types.policy_name.PolicyName"
    """<p>The name of the policy.</p>"""
    policy_version: "capo_opensearchserverless.types.policy_version.PolicyVersion"
    """<p>The version of the policy being updated.</p>"""
    description: NotRequired[
        "capo_opensearchserverless.types.policy_description.PolicyDescription"
    ]
    """<p>A description of the lifecycle policy.</p>"""
    policy: NotRequired[
        "capo_opensearchserverless.types.policy_document.PolicyDocument"
    ]
    """<p>The JSON policy document to use as the content for the lifecycle policy.</p>"""
    client_token: NotRequired[
        "capo_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateLifecyclePolicyRequest) -> dict:
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


def deserialize_aws_json_1_0(data: dict) -> UpdateLifecyclePolicyRequest:
    out: UpdateLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("UpdateLifecyclePolicyRequest.type required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateLifecyclePolicyRequest.name required")
    if "policyVersion" in data:
        out["policy_version"] = data["policyVersion"]
    else:
        raise DeserializationError(
            "UpdateLifecyclePolicyRequest.policy_version required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "policy" in data:
        out["policy"] = data["policy"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
