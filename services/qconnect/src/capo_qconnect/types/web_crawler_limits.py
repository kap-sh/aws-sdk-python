"""Generated from Smithy shape ``com.amazonaws.qconnect#WebCrawlerLimits``."""

from typing_extensions import NotRequired, TypedDict


class WebCrawlerLimits(TypedDict, closed=True):
    rate_limit: NotRequired["int"]
    """<p>Rate of web URLs retrieved per minute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebCrawlerLimits) -> dict:
    out: dict = {}
    if "rate_limit" in value:
        out["rateLimit"] = value["rate_limit"]
    return out


def deserialize_json(data: dict) -> WebCrawlerLimits:
    out: WebCrawlerLimits = {}  # type: ignore[typeddict-item]
    if "rateLimit" in data:
        out["rate_limit"] = data["rateLimit"]
    return out
