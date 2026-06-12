"""Generated from Smithy shape ``com.amazonaws.wafv2#RateLimitForwardedIP``."""

from typing import TypedDict


class RateLimitForwardedIP(TypedDict):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RateLimitForwardedIP) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> RateLimitForwardedIP:
    out: RateLimitForwardedIP = {}  # type: ignore[typeddict-item]
    return out
