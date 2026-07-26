"""Generated from Smithy shape ``com.amazonaws.lightsail#GetDistributionBundlesRequest``."""

from typing_extensions import TypedDict


class GetDistributionBundlesRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDistributionBundlesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDistributionBundlesRequest:
    out: GetDistributionBundlesRequest = {}  # type: ignore[typeddict-item]
    return out
