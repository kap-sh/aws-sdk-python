"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#AccessPolicyStats``."""

from typing_extensions import NotRequired, TypedDict


class AccessPolicyStats(TypedDict, closed=True):
    data_policy_count: NotRequired["int"]
    """<p>The number of data access policies in the current account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccessPolicyStats) -> dict:
    out: dict = {}
    if "data_policy_count" in value:
        out["DataPolicyCount"] = value["data_policy_count"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AccessPolicyStats:
    out: AccessPolicyStats = {}  # type: ignore[typeddict-item]
    if "DataPolicyCount" in data:
        out["data_policy_count"] = data["DataPolicyCount"]
    return out
