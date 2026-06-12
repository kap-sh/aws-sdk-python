"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateLifecyclePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.client_token
    import aws_sdk_opensearchserverless.types.lifecycle_policy_type
    import aws_sdk_opensearchserverless.types.policy_description
    import aws_sdk_opensearchserverless.types.policy_document
    import aws_sdk_opensearchserverless.types.policy_name


class CreateLifecyclePolicyRequest(TypedDict):
    type: "aws_sdk_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType"
    """<p>The type of lifecycle policy.</p>"""
    name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName"
    """<p>The name of the lifecycle policy.</p>"""
    description: NotRequired[
        "aws_sdk_opensearchserverless.types.policy_description.PolicyDescription"
    ]
    """<p>A description of the lifecycle policy.</p>"""
    policy: "aws_sdk_opensearchserverless.types.policy_document.PolicyDocument"
    """<p>The JSON policy document to use as the content for the lifecycle policy.</p>"""
    client_token: NotRequired[
        "aws_sdk_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateLifecyclePolicyRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["policy"] = value["policy"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateLifecyclePolicyRequest:
    out: CreateLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CreateLifecyclePolicyRequest.type required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateLifecyclePolicyRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "policy" in data:
        out["policy"] = data["policy"]
    else:
        raise DeserializationError("CreateLifecyclePolicyRequest.policy required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
