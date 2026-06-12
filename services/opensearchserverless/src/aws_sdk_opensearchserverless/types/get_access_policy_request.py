"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#GetAccessPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.access_policy_type
    import aws_sdk_opensearchserverless.types.policy_name


class GetAccessPolicyRequest(TypedDict):
    type: "aws_sdk_opensearchserverless.types.access_policy_type.AccessPolicyType"
    """<p>Tye type of policy. Currently, the only supported value is <code>data</code>.</p>"""
    name: "aws_sdk_opensearchserverless.types.policy_name.PolicyName"
    """<p>The name of the access policy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAccessPolicyRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAccessPolicyRequest:
    out: GetAccessPolicyRequest = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("GetAccessPolicyRequest.type required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetAccessPolicyRequest.name required")
    return out
