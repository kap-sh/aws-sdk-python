"""Generated from Smithy shape ``com.amazonaws.apigateway#ThrottleSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.double
    import aws_sdk_api_gateway.types.integer


class ThrottleSettings(TypedDict, closed=True):
    burst_limit: "aws_sdk_api_gateway.types.integer.Integer"
    """<p>The API target request burst rate limit. This allows more requests through for a period of time than the target rate limit.</p>"""
    rate_limit: "aws_sdk_api_gateway.types.double.Double"
    """<p>The API target request rate limit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottleSettings) -> dict:
    out: dict = {}
    out["burstLimit"] = value.get("burst_limit", 0)
    out["rateLimit"] = value.get("rate_limit", 0)
    return out


def deserialize_json(data: dict) -> ThrottleSettings:
    out: ThrottleSettings = {}  # type: ignore[typeddict-item]
    if "burstLimit" in data:
        out["burst_limit"] = data["burstLimit"]
    else:
        out["burst_limit"] = 0
    if "rateLimit" in data:
        out["rate_limit"] = data["rateLimit"]
    else:
        out["rate_limit"] = 0
    return out
