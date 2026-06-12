"""Generated from Smithy shape ``com.amazonaws.ivs#ListPlaybackKeyPairsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs.types.max_playback_key_pair_results
    import aws_sdk_ivs.types.pagination_token


class ListPlaybackKeyPairsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_ivs.types.pagination_token.PaginationToken"]
    """<p>The first key pair to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired[
        "aws_sdk_ivs.types.max_playback_key_pair_results.MaxPlaybackKeyPairResults"
    ]
    """<p>Maximum number of key pairs to return. Default: your service quota or 100, whichever is smaller.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPlaybackKeyPairsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListPlaybackKeyPairsRequest:
    out: ListPlaybackKeyPairsRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
