"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribeChannelDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_transcribe.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.medical_scribe_channel_id
    import aws_sdk_transcribe.types.medical_scribe_participant_role


class MedicalScribeChannelDefinition(TypedDict, closed=True):
    channel_id: (
        "aws_sdk_transcribe.types.medical_scribe_channel_id.MedicalScribeChannelId"
    )
    """<p>Specify the audio channel you want to define.</p>"""
    participant_role: "aws_sdk_transcribe.types.medical_scribe_participant_role.MedicalScribeParticipantRole"
    """<p>Specify the participant that you want to flag. The options are <code>CLINICIAN</code> and <code>PATIENT</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalScribeChannelDefinition) -> dict:
    out: dict = {}
    out["ChannelId"] = value.get("channel_id", 0)
    import aws_sdk_transcribe.types.medical_scribe_participant_role

    out["ParticipantRole"] = (
        aws_sdk_transcribe.types.medical_scribe_participant_role.serialize_aws_json_1_1(
            value["participant_role"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> MedicalScribeChannelDefinition:
    out: MedicalScribeChannelDefinition = {}  # type: ignore[typeddict-item]
    if "ChannelId" in data:
        out["channel_id"] = data["ChannelId"]
    else:
        out["channel_id"] = 0
    if "ParticipantRole" in data:
        import aws_sdk_transcribe.types.medical_scribe_participant_role

        out["participant_role"] = (
            aws_sdk_transcribe.types.medical_scribe_participant_role.deserialize_aws_json_1_1(
                data["ParticipantRole"]
            )
        )
    else:
        raise DeserializationError(
            "MedicalScribeChannelDefinition.participant_role required"
        )
    return out
