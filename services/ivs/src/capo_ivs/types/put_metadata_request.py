"""Generated from Smithy shape ``com.amazonaws.ivs#PutMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs.types.channel_arn
    import capo_ivs.types.stream_metadata


class PutMetadataRequest(TypedDict, closed=True):
    channel_arn: "capo_ivs.types.channel_arn.ChannelArn"
    """<p>ARN of the channel into which metadata is inserted. This channel must have an active stream.</p>"""
    metadata: "capo_ivs.types.stream_metadata.StreamMetadata"
    """<p>Metadata to insert into the stream. Maximum: 1 KB per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutMetadataRequest) -> dict:
    out: dict = {}
    out["channelArn"] = value["channel_arn"]
    out["metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> PutMetadataRequest:
    out: PutMetadataRequest = {}  # type: ignore[typeddict-item]
    if "channelArn" in data:
        out["channel_arn"] = data["channelArn"]
    else:
        raise DeserializationError("PutMetadataRequest.channel_arn required")
    if "metadata" in data:
        out["metadata"] = data["metadata"]
    else:
        raise DeserializationError("PutMetadataRequest.metadata required")
    return out
