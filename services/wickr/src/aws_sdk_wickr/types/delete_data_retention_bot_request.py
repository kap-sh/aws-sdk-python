"""Generated from Smithy shape ``com.amazonaws.wickr#DeleteDataRetentionBotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.network_id


class DeleteDataRetentionBotRequest(TypedDict, closed=True):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network from which the data retention bot will be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataRetentionBotRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataRetentionBotRequest:
    out: DeleteDataRetentionBotRequest = {}  # type: ignore[typeddict-item]
    return out
