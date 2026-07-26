"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#SearchResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudsearch_domain.types.facets
    import capo_cloudsearch_domain.types.hits
    import capo_cloudsearch_domain.types.search_status
    import capo_cloudsearch_domain.types.stats


class SearchResponse(TypedDict, closed=True):
    status: NotRequired["capo_cloudsearch_domain.types.search_status.SearchStatus"]
    """<p>The status information returned for the search request.</p>"""
    hits: NotRequired["capo_cloudsearch_domain.types.hits.Hits"]
    """<p>The documents that match the search criteria.</p>"""
    facets: NotRequired["capo_cloudsearch_domain.types.facets.Facets"]
    """<p>The requested facet information.</p>"""
    stats: NotRequired["capo_cloudsearch_domain.types.stats.Stats"]
    """<p>The requested field statistics information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_cloudsearch_domain.types.search_status

        out["status"] = capo_cloudsearch_domain.types.search_status.serialize_json(
            value["status"]
        )
    if "hits" in value:
        import capo_cloudsearch_domain.types.hits

        out["hits"] = capo_cloudsearch_domain.types.hits.serialize_json(value["hits"])
    if "facets" in value:
        import capo_cloudsearch_domain.types.facets

        out["facets"] = capo_cloudsearch_domain.types.facets.serialize_json(
            value["facets"]
        )
    if "stats" in value:
        import capo_cloudsearch_domain.types.stats

        out["stats"] = capo_cloudsearch_domain.types.stats.serialize_json(
            value["stats"]
        )
    return out


def deserialize_json(data: dict) -> SearchResponse:
    out: SearchResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_cloudsearch_domain.types.search_status

        out["status"] = capo_cloudsearch_domain.types.search_status.deserialize_json(
            data["status"]
        )
    if "hits" in data:
        import capo_cloudsearch_domain.types.hits

        out["hits"] = capo_cloudsearch_domain.types.hits.deserialize_json(data["hits"])
    if "facets" in data:
        import capo_cloudsearch_domain.types.facets

        out["facets"] = capo_cloudsearch_domain.types.facets.deserialize_json(
            data["facets"]
        )
    if "stats" in data:
        import capo_cloudsearch_domain.types.stats

        out["stats"] = capo_cloudsearch_domain.types.stats.deserialize_json(
            data["stats"]
        )
    return out
