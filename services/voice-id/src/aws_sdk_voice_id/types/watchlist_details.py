"""Generated from Smithy shape ``com.amazonaws.voiceid#WatchlistDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.watchlist_id


class WatchlistDetails(TypedDict):
    default_watchlist_id: "aws_sdk_voice_id.types.watchlist_id.WatchlistId"
    """<p>The identifier of the default watchlist.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WatchlistDetails) -> dict:
    out: dict = {}
    out["DefaultWatchlistId"] = value["default_watchlist_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WatchlistDetails:
    out: WatchlistDetails = {}  # type: ignore[typeddict-item]
    if "DefaultWatchlistId" in data:
        out["default_watchlist_id"] = data["DefaultWatchlistId"]
    else:
        raise DeserializationError("WatchlistDetails.default_watchlist_id required")
    return out
