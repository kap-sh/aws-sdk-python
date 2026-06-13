"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#DeleteMLInputChannelDataRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.ml_input_channel_arn
    import aws_sdk_cleanroomsml.types.uuid


class DeleteMLInputChannelDataRequest(TypedDict):
    ml_input_channel_arn: (
        "aws_sdk_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn"
    )
    """<p>The Amazon Resource Name (ARN) of the ML input channel that you want to delete.</p>"""
    membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the membership that contains the ML input channel you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMLInputChannelDataRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMLInputChannelDataRequest:
    out: DeleteMLInputChannelDataRequest = {}  # type: ignore[typeddict-item]
    return out
