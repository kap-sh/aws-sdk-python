"""Generated from Smithy shape ``com.amazonaws.location#SearchPlaceIndexForTextResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.search_for_text_result_list
    import aws_sdk_location.types.search_place_index_for_text_summary


class SearchPlaceIndexForTextResponse(TypedDict):
    summary: "aws_sdk_location.types.search_place_index_for_text_summary.SearchPlaceIndexForTextSummary"
    """<p>Contains a summary of the request. Echoes the input values for <code>BiasPosition</code>, <code>FilterBBox</code>, <code>FilterCountries</code>, <code>Language</code>, <code>MaxResults</code>, and <code>Text</code>. Also includes the <code>DataSource</code> of the place index and the bounding box, <code>ResultBBox</code>, which surrounds the search results. </p>"""
    results: (
        "aws_sdk_location.types.search_for_text_result_list.SearchForTextResultList"
    )
    """<p>A list of Places matching the input text. Each result contains additional information about the specific point of interest. </p> <p>Not all response properties are included with all responses. Some properties may only be returned by specific data partners.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchPlaceIndexForTextResponse) -> dict:
    out: dict = {}
    import aws_sdk_location.types.search_place_index_for_text_summary

    out["Summary"] = (
        aws_sdk_location.types.search_place_index_for_text_summary.serialize_json(
            value["summary"]
        )
    )
    import aws_sdk_location.types.search_for_text_result_list

    out["Results"] = aws_sdk_location.types.search_for_text_result_list.serialize_json(
        value["results"]
    )
    return out


def deserialize_json(data: dict) -> SearchPlaceIndexForTextResponse:
    out: SearchPlaceIndexForTextResponse = {}  # type: ignore[typeddict-item]
    if "Summary" in data:
        import aws_sdk_location.types.search_place_index_for_text_summary

        out["summary"] = (
            aws_sdk_location.types.search_place_index_for_text_summary.deserialize_json(
                data["Summary"]
            )
        )
    else:
        raise DeserializationError("SearchPlaceIndexForTextResponse.summary required")
    if "Results" in data:
        import aws_sdk_location.types.search_for_text_result_list

        out["results"] = (
            aws_sdk_location.types.search_for_text_result_list.deserialize_json(
                data["Results"]
            )
        )
    else:
        raise DeserializationError("SearchPlaceIndexForTextResponse.results required")
    return out
