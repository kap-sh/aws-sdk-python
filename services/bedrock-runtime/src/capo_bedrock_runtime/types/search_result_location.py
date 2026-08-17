"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#SearchResultLocation``."""

from typing_extensions import NotRequired, TypedDict


class SearchResultLocation(TypedDict, closed=True):
    search_result_index: NotRequired["int"]
    """<p>The index of the search result content block where the cited content is found.</p>"""
    start: NotRequired["int"]
    """<p>The starting position in the content array where the cited content begins.</p>"""
    end: NotRequired["int"]
    """<p>The ending position in the content array where the cited content ends.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResultLocation) -> dict:
    out: dict = {}
    if "search_result_index" in value:
        out["searchResultIndex"] = value["search_result_index"]
    if "start" in value:
        out["start"] = value["start"]
    if "end" in value:
        out["end"] = value["end"]
    return out


def deserialize_json(data: dict) -> SearchResultLocation:
    out: SearchResultLocation = {}  # type: ignore[typeddict-item]
    if data.get("searchResultIndex") is not None:
        out["search_result_index"] = data["searchResultIndex"]
    if data.get("start") is not None:
        out["start"] = data["start"]
    if data.get("end") is not None:
        out["end"] = data["end"]
    return out
