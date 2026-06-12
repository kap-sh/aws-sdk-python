"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#RedundantIngestCredential``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.participant_id
    import aws_sdk_ivs_realtime.types.stream_key


class RedundantIngestCredential(TypedDict):
    participant_id: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_id.ParticipantId"
    ]
    """<p>ID of the participant within the stage.</p>"""
    stream_key: NotRequired["aws_sdk_ivs_realtime.types.stream_key.StreamKey"]
    """<p>Ingest-key value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedundantIngestCredential) -> dict:
    out: dict = {}
    if "participant_id" in value:
        out["participantId"] = value["participant_id"]
    if "stream_key" in value:
        out["streamKey"] = value["stream_key"]
    return out


def deserialize_json(data: dict) -> RedundantIngestCredential:
    out: RedundantIngestCredential = {}  # type: ignore[typeddict-item]
    if "participantId" in data:
        out["participant_id"] = data["participantId"]
    if "streamKey" in data:
        out["stream_key"] = data["streamKey"]
    return out
