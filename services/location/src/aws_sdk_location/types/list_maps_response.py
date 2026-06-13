"""Generated from Smithy shape ``com.amazonaws.location#ListMapsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.list_maps_response_entry_list
    import aws_sdk_location.types.token


class ListMapsResponse(TypedDict):
    entries: (
        "aws_sdk_location.types.list_maps_response_entry_list.ListMapsResponseEntryList"
    )
    """<p>Contains a list of maps in your Amazon Web Services account</p>"""
    next_token: NotRequired["aws_sdk_location.types.token.Token"]
    """<p>A pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMapsResponse) -> dict:
    out: dict = {}
    import aws_sdk_location.types.list_maps_response_entry_list

    out["Entries"] = (
        aws_sdk_location.types.list_maps_response_entry_list.serialize_json(
            value["entries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMapsResponse:
    out: ListMapsResponse = {}  # type: ignore[typeddict-item]
    if "Entries" in data:
        import aws_sdk_location.types.list_maps_response_entry_list

        out["entries"] = (
            aws_sdk_location.types.list_maps_response_entry_list.deserialize_json(
                data["Entries"]
            )
        )
    else:
        raise DeserializationError("ListMapsResponse.entries required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
