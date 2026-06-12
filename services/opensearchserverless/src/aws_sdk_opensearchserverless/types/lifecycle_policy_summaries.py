"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#LifecyclePolicySummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.lifecycle_policy_summary

LifecyclePolicySummaries: TypeAlias = list[
    "aws_sdk_opensearchserverless.types.lifecycle_policy_summary.LifecyclePolicySummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LifecyclePolicySummaries) -> list:
    import aws_sdk_opensearchserverless.types.lifecycle_policy_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_opensearchserverless.types.lifecycle_policy_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LifecyclePolicySummaries:
    import aws_sdk_opensearchserverless.types.lifecycle_policy_summary

    out: LifecyclePolicySummaries = []
    for item in data:
        out.append(
            aws_sdk_opensearchserverless.types.lifecycle_policy_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
