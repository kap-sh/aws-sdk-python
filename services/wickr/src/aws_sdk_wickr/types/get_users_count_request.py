"""Generated from Smithy shape ``com.amazonaws.wickr#GetUsersCountRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.network_id


class GetUsersCountRequest(TypedDict):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network for which to retrieve user counts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUsersCountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUsersCountRequest:
    out: GetUsersCountRequest = {}  # type: ignore[typeddict-item]
    return out
