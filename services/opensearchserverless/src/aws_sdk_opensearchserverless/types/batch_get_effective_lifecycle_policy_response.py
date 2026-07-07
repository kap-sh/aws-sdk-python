"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#BatchGetEffectiveLifecyclePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.effective_lifecycle_policy_details
    import aws_sdk_opensearchserverless.types.effective_lifecycle_policy_error_details


class BatchGetEffectiveLifecyclePolicyResponse(TypedDict, closed=True):
    effective_lifecycle_policy_details: NotRequired[
        "aws_sdk_opensearchserverless.types.effective_lifecycle_policy_details.EffectiveLifecyclePolicyDetails"
    ]
    """<p>A list of lifecycle policies applied to the OpenSearch Serverless indexes.</p>"""
    effective_lifecycle_policy_error_details: NotRequired[
        "aws_sdk_opensearchserverless.types.effective_lifecycle_policy_error_details.EffectiveLifecyclePolicyErrorDetails"
    ]
    """<p>A list of resources for which retrieval failed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetEffectiveLifecyclePolicyResponse) -> dict:
    out: dict = {}
    if "effective_lifecycle_policy_details" in value:
        import aws_sdk_opensearchserverless.types.effective_lifecycle_policy_details

        out["effectiveLifecyclePolicyDetails"] = (
            aws_sdk_opensearchserverless.types.effective_lifecycle_policy_details.serialize_aws_json_1_0(
                value["effective_lifecycle_policy_details"]
            )
        )
    if "effective_lifecycle_policy_error_details" in value:
        import aws_sdk_opensearchserverless.types.effective_lifecycle_policy_error_details

        out["effectiveLifecyclePolicyErrorDetails"] = (
            aws_sdk_opensearchserverless.types.effective_lifecycle_policy_error_details.serialize_aws_json_1_0(
                value["effective_lifecycle_policy_error_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetEffectiveLifecyclePolicyResponse:
    out: BatchGetEffectiveLifecyclePolicyResponse = {}  # type: ignore[typeddict-item]
    if "effectiveLifecyclePolicyDetails" in data:
        import aws_sdk_opensearchserverless.types.effective_lifecycle_policy_details

        out["effective_lifecycle_policy_details"] = (
            aws_sdk_opensearchserverless.types.effective_lifecycle_policy_details.deserialize_aws_json_1_0(
                data["effectiveLifecyclePolicyDetails"]
            )
        )
    if "effectiveLifecyclePolicyErrorDetails" in data:
        import aws_sdk_opensearchserverless.types.effective_lifecycle_policy_error_details

        out["effective_lifecycle_policy_error_details"] = (
            aws_sdk_opensearchserverless.types.effective_lifecycle_policy_error_details.deserialize_aws_json_1_0(
                data["effectiveLifecyclePolicyErrorDetails"]
            )
        )
    return out
