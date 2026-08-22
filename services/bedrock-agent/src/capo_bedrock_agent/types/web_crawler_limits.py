"""Generated from Smithy shape ``com.amazonaws.bedrockagent#WebCrawlerLimits``."""

from typing_extensions import NotRequired, TypedDict


class WebCrawlerLimits(TypedDict, closed=True):
    rate_limit: NotRequired["int"]
    """<p>The max rate at which pages are crawled, up to 300 per minute per host.</p>"""
    max_pages: NotRequired["int"]
    """<p> The max number of web pages crawled from your source URLs, up to 25,000 pages. If the web pages exceed this limit, the data source sync will fail and no web pages will be ingested. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebCrawlerLimits) -> dict:
    out: dict = {}
    if "rate_limit" in value:
        out["rateLimit"] = value["rate_limit"]
    if "max_pages" in value:
        out["maxPages"] = value["max_pages"]
    return out


def deserialize_json(data: dict) -> WebCrawlerLimits:
    out: WebCrawlerLimits = {}  # type: ignore[typeddict-item]
    if data.get("rateLimit") is not None:
        out["rate_limit"] = data["rateLimit"]
    if data.get("maxPages") is not None:
        out["max_pages"] = data["maxPages"]
    return out
