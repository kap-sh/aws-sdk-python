"""Generated from Smithy shape ``com.amazonaws.location#ListPlaceIndexesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.list_place_indexes_response_entry_list
    import aws_sdk_location.types.token


class ListPlaceIndexesResponse(TypedDict):
    entries: "aws_sdk_location.types.list_place_indexes_response_entry_list.ListPlaceIndexesResponseEntryList"
    """<p>Lists the place index resources that exist in your Amazon Web Services account</p>"""
    next_token: NotRequired["aws_sdk_location.types.token.Token"]
    """<p>A pagination token indicating that there are additional pages available. You can use the token in a new request to fetch the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPlaceIndexesResponse) -> dict:
    out: dict = {}
    import aws_sdk_location.types.list_place_indexes_response_entry_list

    out["Entries"] = (
        aws_sdk_location.types.list_place_indexes_response_entry_list.serialize_json(
            value["entries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPlaceIndexesResponse:
    out: ListPlaceIndexesResponse = {}  # type: ignore[typeddict-item]
    if "Entries" in data:
        import aws_sdk_location.types.list_place_indexes_response_entry_list

        out["entries"] = (
            aws_sdk_location.types.list_place_indexes_response_entry_list.deserialize_json(
                data["Entries"]
            )
        )
    else:
        raise DeserializationError("ListPlaceIndexesResponse.entries required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
