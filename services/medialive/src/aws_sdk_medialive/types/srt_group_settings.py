"""Generated from Smithy shape ``com.amazonaws.medialive#SrtGroupSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.input_loss_action_for_udp_out


class SrtGroupSettings(TypedDict, closed=True):
    input_loss_action: NotRequired[
        "aws_sdk_medialive.types.input_loss_action_for_udp_out.InputLossActionForUdpOut"
    ]
    """Specifies behavior of last resort when input video is lost, and no more backup inputs are available. When dropTs is selected the entire transport stream will stop being emitted. When dropProgram is selected the program can be dropped from the transport stream (and replaced with null packets to meet the TS bitrate requirement). Or, when emitProgram is chosen the transport stream will continue to be produced normally with repeat frames, black frames, or slate frames substituted for the absent input video."""


# --- restJson1 ser/de ---
def serialize_json(value: SrtGroupSettings) -> dict:
    out: dict = {}
    if "input_loss_action" in value:
        import aws_sdk_medialive.types.input_loss_action_for_udp_out

        out["inputLossAction"] = (
            aws_sdk_medialive.types.input_loss_action_for_udp_out.serialize_json(
                value["input_loss_action"]
            )
        )
    return out


def deserialize_json(data: dict) -> SrtGroupSettings:
    out: SrtGroupSettings = {}  # type: ignore[typeddict-item]
    if "inputLossAction" in data:
        import aws_sdk_medialive.types.input_loss_action_for_udp_out

        out["input_loss_action"] = (
            aws_sdk_medialive.types.input_loss_action_for_udp_out.deserialize_json(
                data["inputLossAction"]
            )
        )
    return out
