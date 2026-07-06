"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#UpdateStageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.auto_participant_recording_configuration
    import aws_sdk_ivs_realtime.types.stage_arn
    import aws_sdk_ivs_realtime.types.stage_name


class UpdateStageRequest(TypedDict, closed=True):
    arn: "aws_sdk_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the stage to be updated.</p>"""
    name: NotRequired["aws_sdk_ivs_realtime.types.stage_name.StageName"]
    """<p>Name of the stage to be updated.</p>"""
    auto_participant_recording_configuration: NotRequired[
        "aws_sdk_ivs_realtime.types.auto_participant_recording_configuration.AutoParticipantRecordingConfiguration"
    ]
    """<p>Configuration object for individual participant recording, to attach to the stage. Note that this cannot be updated while recording is active.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateStageRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "auto_participant_recording_configuration" in value:
        import aws_sdk_ivs_realtime.types.auto_participant_recording_configuration

        out["autoParticipantRecordingConfiguration"] = (
            aws_sdk_ivs_realtime.types.auto_participant_recording_configuration.serialize_json(
                value["auto_participant_recording_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateStageRequest:
    out: UpdateStageRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateStageRequest.arn required")
    if "name" in data:
        out["name"] = data["name"]
    if "autoParticipantRecordingConfiguration" in data:
        import aws_sdk_ivs_realtime.types.auto_participant_recording_configuration

        out["auto_participant_recording_configuration"] = (
            aws_sdk_ivs_realtime.types.auto_participant_recording_configuration.deserialize_json(
                data["autoParticipantRecordingConfiguration"]
            )
        )
    return out
