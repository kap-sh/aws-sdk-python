"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#SecurityPolicySummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchserverless.types.security_policy_summary

SecurityPolicySummaries: TypeAlias = list[
    "capo_opensearchserverless.types.security_policy_summary.SecurityPolicySummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SecurityPolicySummaries) -> list:
    import capo_opensearchserverless.types.security_policy_summary

    out: list = []
    for item in value:
        out.append(
            capo_opensearchserverless.types.security_policy_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SecurityPolicySummaries:
    import capo_opensearchserverless.types.security_policy_summary

    out: SecurityPolicySummaries = []
    for item in data:
        out.append(
            capo_opensearchserverless.types.security_policy_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
