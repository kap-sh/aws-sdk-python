"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#SecurityPolicyStats``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SecurityPolicyStats(TypedDict):
    encryption_policy_count: NotRequired["int"]
    """<p>The number of encryption policies in the current account.</p>"""
    network_policy_count: NotRequired["int"]
    """<p>The number of network policies in the current account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SecurityPolicyStats) -> dict:
    out: dict = {}
    if "encryption_policy_count" in value:
        out["EncryptionPolicyCount"] = value["encryption_policy_count"]
    if "network_policy_count" in value:
        out["NetworkPolicyCount"] = value["network_policy_count"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SecurityPolicyStats:
    out: SecurityPolicyStats = {}  # type: ignore[typeddict-item]
    if "EncryptionPolicyCount" in data:
        out["encryption_policy_count"] = data["EncryptionPolicyCount"]
    if "NetworkPolicyCount" in data:
        out["network_policy_count"] = data["NetworkPolicyCount"]
    return out
