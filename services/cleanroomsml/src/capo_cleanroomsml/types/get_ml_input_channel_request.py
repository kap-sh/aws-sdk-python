"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetMLInputChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.ml_input_channel_arn
    import capo_cleanroomsml.types.uuid


class GetMLInputChannelRequest(TypedDict, closed=True):
    ml_input_channel_arn: (
        "capo_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn"
    )
    """<p>The Amazon Resource Name (ARN) of the ML input channel that you want to get.</p>"""
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the membership that contains the ML input channel that you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMLInputChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMLInputChannelRequest:
    out: GetMLInputChannelRequest = {}  # type: ignore[typeddict-item]
    return out
