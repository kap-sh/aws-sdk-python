"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateAccessPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearchserverless.types.access_policy_type
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.policy_description
    import capo_opensearchserverless.types.policy_document
    import capo_opensearchserverless.types.policy_name


class CreateAccessPolicyRequest(TypedDict, closed=True):
    type: "capo_opensearchserverless.types.access_policy_type.AccessPolicyType"
    """<p>The type of policy.</p>"""
    name: "capo_opensearchserverless.types.policy_name.PolicyName"
    """<p>The name of the policy.</p>"""
    description: NotRequired[
        "capo_opensearchserverless.types.policy_description.PolicyDescription"
    ]
    """<p>A description of the policy. Typically used to store information about the permissions defined in the policy.</p>"""
    policy: "capo_opensearchserverless.types.policy_document.PolicyDocument"
    """<p>The JSON policy document to use as the content for the policy.</p>"""
    client_token: NotRequired[
        "capo_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAccessPolicyRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["policy"] = value["policy"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAccessPolicyRequest:
    out: CreateAccessPolicyRequest = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CreateAccessPolicyRequest.type required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAccessPolicyRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "policy" in data:
        out["policy"] = data["policy"]
    else:
        raise DeserializationError("CreateAccessPolicyRequest.policy required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
