"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#LifecyclePolicyIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchserverless.types.lifecycle_policy_identifier

LifecyclePolicyIdentifiers: TypeAlias = list[
    "capo_opensearchserverless.types.lifecycle_policy_identifier.LifecyclePolicyIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LifecyclePolicyIdentifiers) -> list:
    import capo_opensearchserverless.types.lifecycle_policy_identifier

    out: list = []
    for item in value:
        out.append(
            capo_opensearchserverless.types.lifecycle_policy_identifier.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LifecyclePolicyIdentifiers:
    import capo_opensearchserverless.types.lifecycle_policy_identifier

    out: LifecyclePolicyIdentifiers = []
    for item in data:
        out.append(
            capo_opensearchserverless.types.lifecycle_policy_identifier.deserialize_aws_json_1_0(
                item
            )
        )
    return out
