"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetCollaborationMLInputChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.ml_input_channel_arn
    import aws_sdk_cleanroomsml.types.uuid


class GetCollaborationMLInputChannelRequest(TypedDict):
    ml_input_channel_arn: (
        "aws_sdk_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn"
    )
    """<p>The Amazon Resource Name (ARN) of the ML input channel that you want to get.</p>"""
    collaboration_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the ML input channel that you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCollaborationMLInputChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCollaborationMLInputChannelRequest:
    out: GetCollaborationMLInputChannelRequest = {}  # type: ignore[typeddict-item]
    return out
