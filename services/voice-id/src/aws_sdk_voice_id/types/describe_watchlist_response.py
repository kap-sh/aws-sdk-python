"""Generated from Smithy shape ``com.amazonaws.voiceid#DescribeWatchlistResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.watchlist


class DescribeWatchlistResponse(TypedDict):
    watchlist: NotRequired["aws_sdk_voice_id.types.watchlist.Watchlist"]
    """<p>Information about the specified watchlist.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeWatchlistResponse) -> dict:
    out: dict = {}
    if "watchlist" in value:
        import aws_sdk_voice_id.types.watchlist

        out["Watchlist"] = aws_sdk_voice_id.types.watchlist.serialize_aws_json_1_0(
            value["watchlist"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeWatchlistResponse:
    out: DescribeWatchlistResponse = {}  # type: ignore[typeddict-item]
    if "Watchlist" in data:
        import aws_sdk_voice_id.types.watchlist

        out["watchlist"] = aws_sdk_voice_id.types.watchlist.deserialize_aws_json_1_0(
            data["Watchlist"]
        )
    return out
