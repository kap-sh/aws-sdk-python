"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#LifecyclePolicyStats``."""

from typing import TypedDict

from typing_extensions import NotRequired


class LifecyclePolicyStats(TypedDict):
    retention_policy_count: NotRequired["int"]
    """<p>The number of retention lifecycle policies in the current account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LifecyclePolicyStats) -> dict:
    out: dict = {}
    if "retention_policy_count" in value:
        out["RetentionPolicyCount"] = value["retention_policy_count"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LifecyclePolicyStats:
    out: LifecyclePolicyStats = {}  # type: ignore[typeddict-item]
    if "RetentionPolicyCount" in data:
        out["retention_policy_count"] = data["RetentionPolicyCount"]
    return out
