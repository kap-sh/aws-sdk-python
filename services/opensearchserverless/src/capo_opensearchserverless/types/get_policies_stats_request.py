"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#GetPoliciesStatsRequest``."""

from typing_extensions import TypedDict


class GetPoliciesStatsRequest(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPoliciesStatsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPoliciesStatsRequest:
    out: GetPoliciesStatsRequest = {}  # type: ignore[typeddict-item]
    return out
