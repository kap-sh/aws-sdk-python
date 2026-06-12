"""Generated from Smithy shape ``com.amazonaws.wickr#GetBotsCountRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.network_id


class GetBotsCountRequest(TypedDict):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network for which to retrieve bot counts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBotsCountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBotsCountRequest:
    out: GetBotsCountRequest = {}  # type: ignore[typeddict-item]
    return out
