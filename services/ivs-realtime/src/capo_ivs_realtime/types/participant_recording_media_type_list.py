"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantRecordingMediaTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs_realtime.types.participant_recording_media_type

ParticipantRecordingMediaTypeList: TypeAlias = list[
    "capo_ivs_realtime.types.participant_recording_media_type.ParticipantRecordingMediaType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantRecordingMediaTypeList) -> list:
    import capo_ivs_realtime.types.participant_recording_media_type

    out: list = []
    for item in value:
        out.append(
            capo_ivs_realtime.types.participant_recording_media_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ParticipantRecordingMediaTypeList:
    import capo_ivs_realtime.types.participant_recording_media_type

    out: ParticipantRecordingMediaTypeList = []
    for item in data:
        out.append(
            capo_ivs_realtime.types.participant_recording_media_type.deserialize_json(
                item
            )
        )
    return out
