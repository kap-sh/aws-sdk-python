"""Generated from Smithy shape ``com.amazonaws.voiceid#UpdateWatchlistResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.watchlist


class UpdateWatchlistResponse(TypedDict, closed=True):
    watchlist: NotRequired["aws_sdk_voice_id.types.watchlist.Watchlist"]
    """<p>Details about the updated watchlist.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateWatchlistResponse) -> dict:
    out: dict = {}
    if "watchlist" in value:
        import aws_sdk_voice_id.types.watchlist

        out["Watchlist"] = aws_sdk_voice_id.types.watchlist.serialize_aws_json_1_0(
            value["watchlist"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateWatchlistResponse:
    out: UpdateWatchlistResponse = {}  # type: ignore[typeddict-item]
    if "Watchlist" in data:
        import aws_sdk_voice_id.types.watchlist

        out["watchlist"] = aws_sdk_voice_id.types.watchlist.deserialize_aws_json_1_0(
            data["Watchlist"]
        )
    return out
