"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#SecurityConfigSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchserverless.types.security_config_summary

SecurityConfigSummaries: TypeAlias = list[
    "capo_opensearchserverless.types.security_config_summary.SecurityConfigSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SecurityConfigSummaries) -> list:
    import capo_opensearchserverless.types.security_config_summary

    out: list = []
    for item in value:
        out.append(
            capo_opensearchserverless.types.security_config_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SecurityConfigSummaries:
    import capo_opensearchserverless.types.security_config_summary

    out: SecurityConfigSummaries = []
    for item in data:
        out.append(
            capo_opensearchserverless.types.security_config_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
