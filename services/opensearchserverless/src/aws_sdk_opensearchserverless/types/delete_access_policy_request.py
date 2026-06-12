"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#DeleteAccessPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.access_policy_type
    import aws_sdk_opensearchserverless.types.client_token
    import aws_sdk_opensearchserverless.types.policy_name


class DeleteAccessPolicyRequest(TypedDict):
    type: "aws_sdk_opensearchserverless.types.access_policy_type.AccessPolicyType"
    """<p>The type of policy.</p>"""
    name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName"
    """<p>The name of the policy to delete.</p>"""
    client_token: NotRequired[
        "aws_sdk_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAccessPolicyRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["name"] = value["name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAccessPolicyRequest:
    out: DeleteAccessPolicyRequest = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("DeleteAccessPolicyRequest.type required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteAccessPolicyRequest.name required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
