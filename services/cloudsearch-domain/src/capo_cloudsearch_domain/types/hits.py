"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#Hits``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudsearch_domain.types.hit_list
    import capo_cloudsearch_domain.types.long
    import capo_cloudsearch_domain.types.string


class Hits(TypedDict, closed=True):
    found: "capo_cloudsearch_domain.types.long.Long"
    """<p>The total number of documents that match the search request.</p>"""
    start: "capo_cloudsearch_domain.types.long.Long"
    """<p>The index of the first matching document.</p>"""
    cursor: NotRequired["capo_cloudsearch_domain.types.string.String"]
    """<p>A cursor that can be used to retrieve the next set of matching documents when you want to page through a large result set.</p>"""
    hit: NotRequired["capo_cloudsearch_domain.types.hit_list.HitList"]
    """<p>A document that matches the search request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Hits) -> dict:
    out: dict = {}
    out["found"] = value.get("found", 0)
    out["start"] = value.get("start", 0)
    if "cursor" in value:
        out["cursor"] = value["cursor"]
    if "hit" in value:
        import capo_cloudsearch_domain.types.hit_list

        out["hit"] = capo_cloudsearch_domain.types.hit_list.serialize_json(value["hit"])
    return out


def deserialize_json(data: dict) -> Hits:
    out: Hits = {}  # type: ignore[typeddict-item]
    if "found" in data:
        out["found"] = data["found"]
    else:
        out["found"] = 0
    if "start" in data:
        out["start"] = data["start"]
    else:
        out["start"] = 0
    if "cursor" in data:
        out["cursor"] = data["cursor"]
    if "hit" in data:
        import capo_cloudsearch_domain.types.hit_list

        out["hit"] = capo_cloudsearch_domain.types.hit_list.deserialize_json(
            data["hit"]
        )
    return out
