"""Generated from Smithy shape ``com.amazonaws.voiceid#UpdateWatchlistRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.watchlist_description
    import capo_voice_id.types.watchlist_id
    import capo_voice_id.types.watchlist_name


class UpdateWatchlistRequest(TypedDict, closed=True):
    domain_id: "capo_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain that contains the watchlist.</p>"""
    watchlist_id: "capo_voice_id.types.watchlist_id.WatchlistId"
    """<p>The identifier of the watchlist to be updated.</p>"""
    name: NotRequired["capo_voice_id.types.watchlist_name.WatchlistName"]
    """<p>The name of the watchlist.</p>"""
    description: NotRequired[
        "capo_voice_id.types.watchlist_description.WatchlistDescription"
    ]
    """<p>A brief description about this watchlist.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateWatchlistRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    out["WatchlistId"] = value["watchlist_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateWatchlistRequest:
    out: UpdateWatchlistRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    else:
        raise DeserializationError("UpdateWatchlistRequest.domain_id required")
    if "WatchlistId" in data:
        out["watchlist_id"] = data["WatchlistId"]
    else:
        raise DeserializationError("UpdateWatchlistRequest.watchlist_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
