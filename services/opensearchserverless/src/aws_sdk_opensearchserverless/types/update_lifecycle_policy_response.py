"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateLifecyclePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.lifecycle_policy_detail


class UpdateLifecyclePolicyResponse(TypedDict):
    lifecycle_policy_detail: NotRequired[
        "aws_sdk_opensearchserverless.types.lifecycle_policy_detail.LifecyclePolicyDetail"
    ]
    """<p>Details about the updated lifecycle policy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateLifecyclePolicyResponse) -> dict:
    out: dict = {}
    if "lifecycle_policy_detail" in value:
        import aws_sdk_opensearchserverless.types.lifecycle_policy_detail

        out["lifecyclePolicyDetail"] = (
            aws_sdk_opensearchserverless.types.lifecycle_policy_detail.serialize_aws_json_1_0(
                value["lifecycle_policy_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateLifecyclePolicyResponse:
    out: UpdateLifecyclePolicyResponse = {}  # type: ignore[typeddict-item]
    if "lifecyclePolicyDetail" in data:
        import aws_sdk_opensearchserverless.types.lifecycle_policy_detail

        out["lifecycle_policy_detail"] = (
            aws_sdk_opensearchserverless.types.lifecycle_policy_detail.deserialize_aws_json_1_0(
                data["lifecyclePolicyDetail"]
            )
        )
    return out
