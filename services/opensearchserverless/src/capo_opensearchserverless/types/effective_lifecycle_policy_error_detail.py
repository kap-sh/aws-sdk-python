"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#EffectiveLifecyclePolicyErrorDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.lifecycle_policy_type
    import capo_opensearchserverless.types.resource


class EffectiveLifecyclePolicyErrorDetail(TypedDict, closed=True):
    type: NotRequired[
        "capo_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType"
    ]
    """<p>The type of lifecycle policy.</p>"""
    resource: NotRequired["capo_opensearchserverless.types.resource.Resource"]
    """<p>The name of OpenSearch Serverless index resource.</p>"""
    error_message: NotRequired["str"]
    """<p>A description of the error. For example, <code>The specified Index resource is not found</code>.</p>"""
    error_code: NotRequired["str"]
    """<p>The error code for the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EffectiveLifecyclePolicyErrorDetail) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "resource" in value:
        out["resource"] = value["resource"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EffectiveLifecyclePolicyErrorDetail:
    out: EffectiveLifecyclePolicyErrorDetail = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "resource" in data:
        out["resource"] = data["resource"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    return out
