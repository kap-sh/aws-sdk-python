"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#LifecyclePolicyErrorDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.lifecycle_policy_type
    import aws_sdk_opensearchserverless.types.policy_name


class LifecyclePolicyErrorDetail(TypedDict):
    type: NotRequired[
        "aws_sdk_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType"
    ]
    """<p>The type of lifecycle policy.</p>"""
    name: NotRequired["aws_sdk_opensearchserverless.types.policy_name.PolicyName"]
    """<p>The name of the lifecycle policy.</p>"""
    error_message: NotRequired["str"]
    """<p>A description of the error. For example, <code>The specified Lifecycle Policy is not found</code>.</p>"""
    error_code: NotRequired["str"]
    """<p>The error code for the request. For example, <code>NOT_FOUND</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LifecyclePolicyErrorDetail) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "name" in value:
        out["name"] = value["name"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LifecyclePolicyErrorDetail:
    out: LifecyclePolicyErrorDetail = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "name" in data:
        out["name"] = data["name"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    return out
