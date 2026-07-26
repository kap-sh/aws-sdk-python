"""Generated from Smithy shape ``com.amazonaws.kinesisvideosignaling#IceServerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_video_signaling.types.ice_server

IceServerList: TypeAlias = list[
    "capo_kinesis_video_signaling.types.ice_server.IceServer"
]


# --- restJson1 ser/de ---
def serialize_json(value: IceServerList) -> list:
    import capo_kinesis_video_signaling.types.ice_server

    out: list = []
    for item in value:
        out.append(capo_kinesis_video_signaling.types.ice_server.serialize_json(item))
    return out


def deserialize_json(data: list) -> IceServerList:
    import capo_kinesis_video_signaling.types.ice_server

    out: IceServerList = []
    for item in data:
        out.append(capo_kinesis_video_signaling.types.ice_server.deserialize_json(item))
    return out
