"""Generated from Smithy shape ``com.amazonaws.rtbfabric#RateLimiterModuleParameters``."""

from typing import TypedDict

from typing_extensions import NotRequired


class RateLimiterModuleParameters(TypedDict):
    tps: NotRequired["float"]
    """<p>The transactions per second rate limit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RateLimiterModuleParameters) -> dict:
    out: dict = {}
    if "tps" in value:
        out["tps"] = value["tps"]
    return out


def deserialize_json(data: dict) -> RateLimiterModuleParameters:
    out: RateLimiterModuleParameters = {}  # type: ignore[typeddict-item]
    if "tps" in data:
        out["tps"] = data["tps"]
    return out
