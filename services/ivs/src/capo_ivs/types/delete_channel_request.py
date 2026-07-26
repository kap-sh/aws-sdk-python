"""Generated from Smithy shape ``com.amazonaws.ivs#DeleteChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs.types.channel_arn


class DeleteChannelRequest(TypedDict, closed=True):
    arn: "capo_ivs.types.channel_arn.ChannelArn"
    """<p>ARN of the channel to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteChannelRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteChannelRequest:
    out: DeleteChannelRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteChannelRequest.arn required")
    return out
