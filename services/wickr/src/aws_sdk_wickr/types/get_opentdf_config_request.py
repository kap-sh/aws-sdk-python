"""Generated from Smithy shape ``com.amazonaws.wickr#GetOpentdfConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.network_id


class GetOpentdfConfigRequest(TypedDict):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network for which OpenTDF integration will be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOpentdfConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOpentdfConfigRequest:
    out: GetOpentdfConfigRequest = {}  # type: ignore[typeddict-item]
    return out
