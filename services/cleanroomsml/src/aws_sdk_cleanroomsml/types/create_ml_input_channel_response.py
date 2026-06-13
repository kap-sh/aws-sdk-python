"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CreateMLInputChannelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.ml_input_channel_arn


class CreateMLInputChannelResponse(TypedDict):
    ml_input_channel_arn: (
        "aws_sdk_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn"
    )
    """<p>The Amazon Resource Name (ARN) of the ML input channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMLInputChannelResponse) -> dict:
    out: dict = {}
    out["mlInputChannelArn"] = value["ml_input_channel_arn"]
    return out


def deserialize_json(data: dict) -> CreateMLInputChannelResponse:
    out: CreateMLInputChannelResponse = {}  # type: ignore[typeddict-item]
    if "mlInputChannelArn" in data:
        out["ml_input_channel_arn"] = data["mlInputChannelArn"]
    else:
        raise DeserializationError(
            "CreateMLInputChannelResponse.ml_input_channel_arn required"
        )
    return out
