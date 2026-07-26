"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#EffectiveLifecyclePolicyErrorDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchserverless.types.effective_lifecycle_policy_error_detail

EffectiveLifecyclePolicyErrorDetails: TypeAlias = list[
    "capo_opensearchserverless.types.effective_lifecycle_policy_error_detail.EffectiveLifecyclePolicyErrorDetail"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EffectiveLifecyclePolicyErrorDetails) -> list:
    import capo_opensearchserverless.types.effective_lifecycle_policy_error_detail

    out: list = []
    for item in value:
        out.append(
            capo_opensearchserverless.types.effective_lifecycle_policy_error_detail.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EffectiveLifecyclePolicyErrorDetails:
    import capo_opensearchserverless.types.effective_lifecycle_policy_error_detail

    out: EffectiveLifecyclePolicyErrorDetails = []
    for item in data:
        out.append(
            capo_opensearchserverless.types.effective_lifecycle_policy_error_detail.deserialize_aws_json_1_0(
                item
            )
        )
    return out
