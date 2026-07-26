"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#AccessPolicySummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchserverless.types.access_policy_summary

AccessPolicySummaries: TypeAlias = list[
    "capo_opensearchserverless.types.access_policy_summary.AccessPolicySummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccessPolicySummaries) -> list:
    import capo_opensearchserverless.types.access_policy_summary

    out: list = []
    for item in value:
        out.append(
            capo_opensearchserverless.types.access_policy_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AccessPolicySummaries:
    import capo_opensearchserverless.types.access_policy_summary

    out: AccessPolicySummaries = []
    for item in data:
        out.append(
            capo_opensearchserverless.types.access_policy_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
