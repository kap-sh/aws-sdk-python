"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetEncoderConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.encoder_configuration


class GetEncoderConfigurationResponse(TypedDict, closed=True):
    encoder_configuration: NotRequired[
        "aws_sdk_ivs_realtime.types.encoder_configuration.EncoderConfiguration"
    ]
    """<p>The EncoderConfiguration that was returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEncoderConfigurationResponse) -> dict:
    out: dict = {}
    if "encoder_configuration" in value:
        import aws_sdk_ivs_realtime.types.encoder_configuration

        out["encoderConfiguration"] = (
            aws_sdk_ivs_realtime.types.encoder_configuration.serialize_json(
                value["encoder_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetEncoderConfigurationResponse:
    out: GetEncoderConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "encoderConfiguration" in data:
        import aws_sdk_ivs_realtime.types.encoder_configuration

        out["encoder_configuration"] = (
            aws_sdk_ivs_realtime.types.encoder_configuration.deserialize_json(
                data["encoderConfiguration"]
            )
        )
    return out
