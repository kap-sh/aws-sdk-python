"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListReceivedDataGrantsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.list_of_received_data_grant_summaries_entry
    import capo_dataexchange.types.next_token


class ListReceivedDataGrantsResponse(TypedDict, closed=True):
    data_grant_summaries: NotRequired[
        "capo_dataexchange.types.list_of_received_data_grant_summaries_entry.ListOfReceivedDataGrantSummariesEntry"
    ]
    """<p>An object that contains a list of received data grant information.</p>"""
    next_token: NotRequired["capo_dataexchange.types.next_token.NextToken"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReceivedDataGrantsResponse) -> dict:
    out: dict = {}
    if "data_grant_summaries" in value:
        import capo_dataexchange.types.list_of_received_data_grant_summaries_entry

        out["DataGrantSummaries"] = (
            capo_dataexchange.types.list_of_received_data_grant_summaries_entry.serialize_json(
                value["data_grant_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListReceivedDataGrantsResponse:
    out: ListReceivedDataGrantsResponse = {}  # type: ignore[typeddict-item]
    if "DataGrantSummaries" in data:
        import capo_dataexchange.types.list_of_received_data_grant_summaries_entry

        out["data_grant_summaries"] = (
            capo_dataexchange.types.list_of_received_data_grant_summaries_entry.deserialize_json(
                data["DataGrantSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
