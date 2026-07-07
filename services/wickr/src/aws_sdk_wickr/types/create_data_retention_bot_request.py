"""Generated from Smithy shape ``com.amazonaws.wickr#CreateDataRetentionBotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.network_id


class CreateDataRetentionBotRequest(TypedDict, closed=True):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network where the data retention bot will be created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataRetentionBotRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CreateDataRetentionBotRequest:
    out: CreateDataRetentionBotRequest = {}  # type: ignore[typeddict-item]
    return out
