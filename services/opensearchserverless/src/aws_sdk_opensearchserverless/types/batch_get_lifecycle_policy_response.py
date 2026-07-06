"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#BatchGetLifecyclePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.lifecycle_policy_details
    import aws_sdk_opensearchserverless.types.lifecycle_policy_error_details


class BatchGetLifecyclePolicyResponse(TypedDict, closed=True):
    lifecycle_policy_details: NotRequired[
        "aws_sdk_opensearchserverless.types.lifecycle_policy_details.LifecyclePolicyDetails"
    ]
    """<p>A list of lifecycle policies matched to the input policy name and policy type.</p>"""
    lifecycle_policy_error_details: NotRequired[
        "aws_sdk_opensearchserverless.types.lifecycle_policy_error_details.LifecyclePolicyErrorDetails"
    ]
    """<p>A list of lifecycle policy names and policy types for which retrieval failed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetLifecyclePolicyResponse) -> dict:
    out: dict = {}
    if "lifecycle_policy_details" in value:
        import aws_sdk_opensearchserverless.types.lifecycle_policy_details

        out["lifecyclePolicyDetails"] = (
            aws_sdk_opensearchserverless.types.lifecycle_policy_details.serialize_aws_json_1_0(
                value["lifecycle_policy_details"]
            )
        )
    if "lifecycle_policy_error_details" in value:
        import aws_sdk_opensearchserverless.types.lifecycle_policy_error_details

        out["lifecyclePolicyErrorDetails"] = (
            aws_sdk_opensearchserverless.types.lifecycle_policy_error_details.serialize_aws_json_1_0(
                value["lifecycle_policy_error_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetLifecyclePolicyResponse:
    out: BatchGetLifecyclePolicyResponse = {}  # type: ignore[typeddict-item]
    if "lifecyclePolicyDetails" in data:
        import aws_sdk_opensearchserverless.types.lifecycle_policy_details

        out["lifecycle_policy_details"] = (
            aws_sdk_opensearchserverless.types.lifecycle_policy_details.deserialize_aws_json_1_0(
                data["lifecyclePolicyDetails"]
            )
        )
    if "lifecyclePolicyErrorDetails" in data:
        import aws_sdk_opensearchserverless.types.lifecycle_policy_error_details

        out["lifecycle_policy_error_details"] = (
            aws_sdk_opensearchserverless.types.lifecycle_policy_error_details.deserialize_aws_json_1_0(
                data["lifecyclePolicyErrorDetails"]
            )
        )
    return out
