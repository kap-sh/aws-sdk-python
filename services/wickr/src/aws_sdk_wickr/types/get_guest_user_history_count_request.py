"""Generated from Smithy shape ``com.amazonaws.wickr#GetGuestUserHistoryCountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.network_id


class GetGuestUserHistoryCountRequest(TypedDict, closed=True):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network for which to retrieve guest user history.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGuestUserHistoryCountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGuestUserHistoryCountRequest:
    out: GetGuestUserHistoryCountRequest = {}  # type: ignore[typeddict-item]
    return out
