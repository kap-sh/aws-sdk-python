"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantRecordingMediaTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.participant_recording_media_type

ParticipantRecordingMediaTypeList: TypeAlias = list[
    "aws_sdk_ivs_realtime.types.participant_recording_media_type.ParticipantRecordingMediaType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantRecordingMediaTypeList) -> list:
    import aws_sdk_ivs_realtime.types.participant_recording_media_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ivs_realtime.types.participant_recording_media_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ParticipantRecordingMediaTypeList:
    import aws_sdk_ivs_realtime.types.participant_recording_media_type

    out: ParticipantRecordingMediaTypeList = []
    for item in data:
        out.append(
            aws_sdk_ivs_realtime.types.participant_recording_media_type.deserialize_json(
                item
            )
        )
    return out
