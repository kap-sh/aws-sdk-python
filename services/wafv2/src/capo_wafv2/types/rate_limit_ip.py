"""Generated from Smithy shape ``com.amazonaws.wafv2#RateLimitIP``."""

from typing_extensions import TypedDict


class RateLimitIP(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RateLimitIP) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> RateLimitIP:
    out: RateLimitIP = {}  # type: ignore[typeddict-item]
    return out
