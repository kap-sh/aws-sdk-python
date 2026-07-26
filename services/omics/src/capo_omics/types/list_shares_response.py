"""Generated from Smithy shape ``com.amazonaws.omics#ListSharesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_omics.types.share_details_list


class ListSharesResponse(TypedDict, closed=True):
    shares: "capo_omics.types.share_details_list.ShareDetailsList"
    """<p>The shares available and their metadata details.</p>"""
    next_token: NotRequired["str"]
    """<p> Next token returned in the response of a previous ListSharesResponse call. Used to get the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSharesResponse) -> dict:
    out: dict = {}
    import capo_omics.types.share_details_list

    out["shares"] = capo_omics.types.share_details_list.serialize_json(value["shares"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSharesResponse:
    out: ListSharesResponse = {}  # type: ignore[typeddict-item]
    if "shares" in data:
        import capo_omics.types.share_details_list

        out["shares"] = capo_omics.types.share_details_list.deserialize_json(
            data["shares"]
        )
    else:
        raise DeserializationError("ListSharesResponse.shares required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
