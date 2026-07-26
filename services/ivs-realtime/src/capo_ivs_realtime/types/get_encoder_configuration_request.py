"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetEncoderConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs_realtime.types.encoder_configuration_arn


class GetEncoderConfigurationRequest(TypedDict, closed=True):
    arn: "capo_ivs_realtime.types.encoder_configuration_arn.EncoderConfigurationArn"
    """<p>ARN of the EncoderConfiguration resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEncoderConfigurationRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetEncoderConfigurationRequest:
    out: GetEncoderConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetEncoderConfigurationRequest.arn required")
    return out
