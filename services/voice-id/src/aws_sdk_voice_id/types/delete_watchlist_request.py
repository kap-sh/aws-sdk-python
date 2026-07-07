"""Generated from Smithy shape ``com.amazonaws.voiceid#DeleteWatchlistRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.domain_id
    import aws_sdk_voice_id.types.watchlist_id


class DeleteWatchlistRequest(TypedDict, closed=True):
    domain_id: "aws_sdk_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain that contains the watchlist.</p>"""
    watchlist_id: "aws_sdk_voice_id.types.watchlist_id.WatchlistId"
    """<p>The identifier of the watchlist to be deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteWatchlistRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    out["WatchlistId"] = value["watchlist_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteWatchlistRequest:
    out: DeleteWatchlistRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    else:
        raise DeserializationError("DeleteWatchlistRequest.domain_id required")
    if "WatchlistId" in data:
        out["watchlist_id"] = data["WatchlistId"]
    else:
        raise DeserializationError("DeleteWatchlistRequest.watchlist_id required")
    return out
