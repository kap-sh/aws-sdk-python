"""Generated from Smithy shape ``com.amazonaws.voiceid#CreateWatchlistResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.watchlist


class CreateWatchlistResponse(TypedDict, closed=True):
    watchlist: NotRequired["aws_sdk_voice_id.types.watchlist.Watchlist"]
    """<p>Information about the newly created watchlist.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateWatchlistResponse) -> dict:
    out: dict = {}
    if "watchlist" in value:
        import aws_sdk_voice_id.types.watchlist

        out["Watchlist"] = aws_sdk_voice_id.types.watchlist.serialize_aws_json_1_0(
            value["watchlist"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateWatchlistResponse:
    out: CreateWatchlistResponse = {}  # type: ignore[typeddict-item]
    if "Watchlist" in data:
        import aws_sdk_voice_id.types.watchlist

        out["watchlist"] = aws_sdk_voice_id.types.watchlist.deserialize_aws_json_1_0(
            data["Watchlist"]
        )
    return out
