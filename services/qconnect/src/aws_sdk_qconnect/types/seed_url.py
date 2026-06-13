"""Generated from Smithy shape ``com.amazonaws.qconnect#SeedUrl``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.web_url


class SeedUrl(TypedDict):
    url: NotRequired["aws_sdk_qconnect.types.web_url.WebUrl"]
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
