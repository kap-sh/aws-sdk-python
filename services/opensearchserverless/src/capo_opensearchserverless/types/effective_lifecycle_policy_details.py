"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#EffectiveLifecyclePolicyDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchserverless.types.effective_lifecycle_policy_detail

EffectiveLifecyclePolicyDetails: TypeAlias = list[
    "capo_opensearchserverless.types.effective_lifecycle_policy_detail.EffectiveLifecyclePolicyDetail"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EffectiveLifecyclePolicyDetails) -> list:
    import capo_opensearchserverless.types.effective_lifecycle_policy_detail

    out: list = []
    for item in value:
        out.append(
            capo_opensearchserverless.types.effective_lifecycle_policy_detail.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EffectiveLifecyclePolicyDetails:
    import capo_opensearchserverless.types.effective_lifecycle_policy_detail

    out: EffectiveLifecyclePolicyDetails = []
    for item in data:
        out.append(
            capo_opensearchserverless.types.effective_lifecycle_policy_detail.deserialize_aws_json_1_0(
                item
            )
        )
    return out
