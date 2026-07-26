"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListPublicKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.max_public_key_results
    import capo_ivs_realtime.types.pagination_token


class ListPublicKeysRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_ivs_realtime.types.pagination_token.PaginationToken"]
    """<p>The first public key to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired[
        "capo_ivs_realtime.types.max_public_key_results.MaxPublicKeyResults"
    ]
    """<p>Maximum number of results to return. Default: 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPublicKeysRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListPublicKeysRequest:
    out: ListPublicKeysRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
