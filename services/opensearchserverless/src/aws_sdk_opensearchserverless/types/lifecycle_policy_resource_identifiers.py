"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#LifecyclePolicyResourceIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.lifecycle_policy_resource_identifier

LifecyclePolicyResourceIdentifiers: TypeAlias = list[
    "aws_sdk_opensearchserverless.types.lifecycle_policy_resource_identifier.LifecyclePolicyResourceIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LifecyclePolicyResourceIdentifiers) -> list:
    import aws_sdk_opensearchserverless.types.lifecycle_policy_resource_identifier

    out: list = []
    for item in value:
        out.append(
            aws_sdk_opensearchserverless.types.lifecycle_policy_resource_identifier.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LifecyclePolicyResourceIdentifiers:
    import aws_sdk_opensearchserverless.types.lifecycle_policy_resource_identifier

    out: LifecyclePolicyResourceIdentifiers = []
    for item in data:
        out.append(
            aws_sdk_opensearchserverless.types.lifecycle_policy_resource_identifier.deserialize_aws_json_1_0(
                item
            )
        )
    return out
