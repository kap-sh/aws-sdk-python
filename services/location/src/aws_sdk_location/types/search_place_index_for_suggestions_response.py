"""Generated from Smithy shape ``com.amazonaws.location#SearchPlaceIndexForSuggestionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.search_for_suggestions_result_list
    import aws_sdk_location.types.search_place_index_for_suggestions_summary


class SearchPlaceIndexForSuggestionsResponse(TypedDict, closed=True):
    summary: "aws_sdk_location.types.search_place_index_for_suggestions_summary.SearchPlaceIndexForSuggestionsSummary"
    """<p>Contains a summary of the request. Echoes the input values for <code>BiasPosition</code>, <code>FilterBBox</code>, <code>FilterCountries</code>, <code>Language</code>, <code>MaxResults</code>, and <code>Text</code>. Also includes the <code>DataSource</code> of the place index. </p>"""
    results: "aws_sdk_location.types.search_for_suggestions_result_list.SearchForSuggestionsResultList"
    """<p>A list of place suggestions that best match the search text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchPlaceIndexForSuggestionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_location.types.search_place_index_for_suggestions_summary

    out["Summary"] = (
        aws_sdk_location.types.search_place_index_for_suggestions_summary.serialize_json(
            value["summary"]
        )
    )
    import aws_sdk_location.types.search_for_suggestions_result_list

    out["Results"] = (
        aws_sdk_location.types.search_for_suggestions_result_list.serialize_json(
            value["results"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchPlaceIndexForSuggestionsResponse:
    out: SearchPlaceIndexForSuggestionsResponse = {}  # type: ignore[typeddict-item]
    if "Summary" in data:
        import aws_sdk_location.types.search_place_index_for_suggestions_summary

        out["summary"] = (
            aws_sdk_location.types.search_place_index_for_suggestions_summary.deserialize_json(
                data["Summary"]
            )
        )
    else:
        raise DeserializationError(
            "SearchPlaceIndexForSuggestionsResponse.summary required"
        )
    if "Results" in data:
        import aws_sdk_location.types.search_for_suggestions_result_list

        out["results"] = (
            aws_sdk_location.types.search_for_suggestions_result_list.deserialize_json(
                data["Results"]
            )
        )
    else:
        raise DeserializationError(
            "SearchPlaceIndexForSuggestionsResponse.results required"
        )
    return out
