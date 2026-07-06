"""Generated from Smithy shape ``com.amazonaws.location#SearchPlaceIndexForPositionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.search_for_position_result_list
    import aws_sdk_location.types.search_place_index_for_position_summary


class SearchPlaceIndexForPositionResponse(TypedDict, closed=True):
    summary: "aws_sdk_location.types.search_place_index_for_position_summary.SearchPlaceIndexForPositionSummary"
    """<p>Contains a summary of the request. Echoes the input values for <code>Position</code>, <code>Language</code>, <code>MaxResults</code>, and the <code>DataSource</code> of the place index. </p>"""
    results: "aws_sdk_location.types.search_for_position_result_list.SearchForPositionResultList"
    """<p>Returns a list of Places closest to the specified position. Each result contains additional information about the Places returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchPlaceIndexForPositionResponse) -> dict:
    out: dict = {}
    import aws_sdk_location.types.search_place_index_for_position_summary

    out["Summary"] = (
        aws_sdk_location.types.search_place_index_for_position_summary.serialize_json(
            value["summary"]
        )
    )
    import aws_sdk_location.types.search_for_position_result_list

    out["Results"] = (
        aws_sdk_location.types.search_for_position_result_list.serialize_json(
            value["results"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchPlaceIndexForPositionResponse:
    out: SearchPlaceIndexForPositionResponse = {}  # type: ignore[typeddict-item]
    if "Summary" in data:
        import aws_sdk_location.types.search_place_index_for_position_summary

        out["summary"] = (
            aws_sdk_location.types.search_place_index_for_position_summary.deserialize_json(
                data["Summary"]
            )
        )
    else:
        raise DeserializationError(
            "SearchPlaceIndexForPositionResponse.summary required"
        )
    if "Results" in data:
        import aws_sdk_location.types.search_for_position_result_list

        out["results"] = (
            aws_sdk_location.types.search_for_position_result_list.deserialize_json(
                data["Results"]
            )
        )
    else:
        raise DeserializationError(
            "SearchPlaceIndexForPositionResponse.results required"
        )
    return out
