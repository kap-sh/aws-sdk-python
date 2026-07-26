"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#WebLocation``."""

from typing_extensions import NotRequired, TypedDict


class WebLocation(TypedDict, closed=True):
    url: NotRequired["str"]
    """<p>The URL that was cited when performing a web search.</p>"""
    domain: NotRequired["str"]
    """<p>The domain that was cited when performing a web search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebLocation) -> dict:
    out: dict = {}
    if "url" in value:
        out["url"] = value["url"]
    if "domain" in value:
        out["domain"] = value["domain"]
    return out


def deserialize_json(data: dict) -> WebLocation:
    out: WebLocation = {}  # type: ignore[typeddict-item]
    if "url" in data:
        out["url"] = data["url"]
    if "domain" in data:
        out["domain"] = data["domain"]
    return out
