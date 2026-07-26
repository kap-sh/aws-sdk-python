"""Generated from Smithy shape ``com.amazonaws.qconnect#SeedUrl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.web_url


class SeedUrl(TypedDict, closed=True):
    url: NotRequired["capo_qconnect.types.web_url.WebUrl"]
    """<p>URL for crawling</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SeedUrl) -> dict:
    out: dict = {}
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> SeedUrl:
    out: SeedUrl = {}  # type: ignore[typeddict-item]
    if "url" in data:
        out["url"] = data["url"]
    return out
