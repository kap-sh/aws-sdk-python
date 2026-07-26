"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#LifecyclePolicyDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchserverless.types.lifecycle_policy_detail

LifecyclePolicyDetails: TypeAlias = list[
    "capo_opensearchserverless.types.lifecycle_policy_detail.LifecyclePolicyDetail"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LifecyclePolicyDetails) -> list:
    import capo_opensearchserverless.types.lifecycle_policy_detail

    out: list = []
    for item in value:
        out.append(
            capo_opensearchserverless.types.lifecycle_policy_detail.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LifecyclePolicyDetails:
    import capo_opensearchserverless.types.lifecycle_policy_detail

    out: LifecyclePolicyDetails = []
    for item in data:
        out.append(
            capo_opensearchserverless.types.lifecycle_policy_detail.deserialize_aws_json_1_0(
                item
            )
        )
    return out
