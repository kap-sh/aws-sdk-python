"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeChannelDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.medical_scribe_channel_id
    import aws_sdk_connecthealth.types.medical_scribe_participant_role


class MedicalScribeChannelDefinition(TypedDict, closed=True):
    channel_id: (
        "aws_sdk_connecthealth.types.medical_scribe_channel_id.MedicalScribeChannelId"
    )
    """<p>The channel identifier</p>"""
    participant_role: "aws_sdk_connecthealth.types.medical_scribe_participant_role.MedicalScribeParticipantRole"
    """<p>The role of the participant on this channel</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeChannelDefinition) -> dict:
    out: dict = {}
    out["channelId"] = value["channel_id"]
    import aws_sdk_connecthealth.types.medical_scribe_participant_role

    out["participantRole"] = (
        aws_sdk_connecthealth.types.medical_scribe_participant_role.serialize_json(
            value["participant_role"]
        )
    )
    return out


def deserialize_json(data: dict) -> MedicalScribeChannelDefinition:
    out: MedicalScribeChannelDefinition = {}  # type: ignore[typeddict-item]
    if "channelId" in data:
        out["channel_id"] = data["channelId"]
    else:
        raise DeserializationError("MedicalScribeChannelDefinition.channel_id required")
    if "participantRole" in data:
        import aws_sdk_connecthealth.types.medical_scribe_participant_role

        out["participant_role"] = (
            aws_sdk_connecthealth.types.medical_scribe_participant_role.deserialize_json(
                data["participantRole"]
            )
        )
    else:
        raise DeserializationError(
            "MedicalScribeChannelDefinition.participant_role required"
        )
    return out
