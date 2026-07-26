"""Generated from Smithy shape ``com.amazonaws.connect#SearchPredefinedAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.approximate_total_count
    import capo_connect.types.next_token2500
    import capo_connect.types.predefined_attribute_search_summary_list


class SearchPredefinedAttributesResponse(TypedDict, closed=True):
    predefined_attributes: NotRequired[
        "capo_connect.types.predefined_attribute_search_summary_list.PredefinedAttributeSearchSummaryList"
    ]
    """<p>Predefined attributes matched by the search criteria.</p>"""
    next_token: NotRequired["capo_connect.types.next_token2500.NextToken2500"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    approximate_total_count: NotRequired[
        "capo_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The approximate number of predefined attributes which matched your search query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchPredefinedAttributesResponse) -> dict:
    out: dict = {}
    if "predefined_attributes" in value:
        import capo_connect.types.predefined_attribute_search_summary_list

        out["PredefinedAttributes"] = (
            capo_connect.types.predefined_attribute_search_summary_list.serialize_json(
                value["predefined_attributes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchPredefinedAttributesResponse:
    out: SearchPredefinedAttributesResponse = {}  # type: ignore[typeddict-item]
    if "PredefinedAttributes" in data:
        import capo_connect.types.predefined_attribute_search_summary_list

        out["predefined_attributes"] = (
            capo_connect.types.predefined_attribute_search_summary_list.deserialize_json(
                data["PredefinedAttributes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
