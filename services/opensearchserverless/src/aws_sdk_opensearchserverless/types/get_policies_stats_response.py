"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#GetPoliciesStatsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.access_policy_stats
    import aws_sdk_opensearchserverless.types.lifecycle_policy_stats
    import aws_sdk_opensearchserverless.types.security_config_stats
    import aws_sdk_opensearchserverless.types.security_policy_stats


class GetPoliciesStatsResponse(TypedDict):
    access_policy_stats: NotRequired[
        "aws_sdk_opensearchserverless.types.access_policy_stats.AccessPolicyStats"
    ]
    """<p>Information about the data access policies in your account.</p>"""
    security_policy_stats: NotRequired[
        "aws_sdk_opensearchserverless.types.security_policy_stats.SecurityPolicyStats"
    ]
    """<p>Information about the security policies in your account.</p>"""
    security_config_stats: NotRequired[
        "aws_sdk_opensearchserverless.types.security_config_stats.SecurityConfigStats"
    ]
    """<p>Information about the security configurations in your account.</p>"""
    lifecycle_policy_stats: NotRequired[
        "aws_sdk_opensearchserverless.types.lifecycle_policy_stats.LifecyclePolicyStats"
    ]
    """<p>Information about the lifecycle policies in your account.</p>"""
    total_policy_count: NotRequired["int"]
    """<p>The total number of OpenSearch Serverless security policies and configurations in your account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPoliciesStatsResponse) -> dict:
    out: dict = {}
    if "access_policy_stats" in value:
        import aws_sdk_opensearchserverless.types.access_policy_stats

        out["AccessPolicyStats"] = (
            aws_sdk_opensearchserverless.types.access_policy_stats.serialize_aws_json_1_0(
                value["access_policy_stats"]
            )
        )
    if "security_policy_stats" in value:
        import aws_sdk_opensearchserverless.types.security_policy_stats

        out["SecurityPolicyStats"] = (
            aws_sdk_opensearchserverless.types.security_policy_stats.serialize_aws_json_1_0(
                value["security_policy_stats"]
            )
        )
    if "security_config_stats" in value:
        import aws_sdk_opensearchserverless.types.security_config_stats

        out["SecurityConfigStats"] = (
            aws_sdk_opensearchserverless.types.security_config_stats.serialize_aws_json_1_0(
                value["security_config_stats"]
            )
        )
    if "lifecycle_policy_stats" in value:
        import aws_sdk_opensearchserverless.types.lifecycle_policy_stats

        out["LifecyclePolicyStats"] = (
            aws_sdk_opensearchserverless.types.lifecycle_policy_stats.serialize_aws_json_1_0(
                value["lifecycle_policy_stats"]
            )
        )
    if "total_policy_count" in value:
        out["TotalPolicyCount"] = value["total_policy_count"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPoliciesStatsResponse:
    out: GetPoliciesStatsResponse = {}  # type: ignore[typeddict-item]
    if "AccessPolicyStats" in data:
        import aws_sdk_opensearchserverless.types.access_policy_stats

        out["access_policy_stats"] = (
            aws_sdk_opensearchserverless.types.access_policy_stats.deserialize_aws_json_1_0(
                data["AccessPolicyStats"]
            )
        )
    if "SecurityPolicyStats" in data:
        import aws_sdk_opensearchserverless.types.security_policy_stats

        out["security_policy_stats"] = (
            aws_sdk_opensearchserverless.types.security_policy_stats.deserialize_aws_json_1_0(
                data["SecurityPolicyStats"]
            )
        )
    if "SecurityConfigStats" in data:
        import aws_sdk_opensearchserverless.types.security_config_stats

        out["security_config_stats"] = (
            aws_sdk_opensearchserverless.types.security_config_stats.deserialize_aws_json_1_0(
                data["SecurityConfigStats"]
            )
        )
    if "LifecyclePolicyStats" in data:
        import aws_sdk_opensearchserverless.types.lifecycle_policy_stats

        out["lifecycle_policy_stats"] = (
            aws_sdk_opensearchserverless.types.lifecycle_policy_stats.deserialize_aws_json_1_0(
                data["LifecyclePolicyStats"]
            )
        )
    if "TotalPolicyCount" in data:
        out["total_policy_count"] = data["TotalPolicyCount"]
    return out
