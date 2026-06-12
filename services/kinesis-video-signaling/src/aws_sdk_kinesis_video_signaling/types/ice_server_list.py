"""Generated from Smithy shape ``com.amazonaws.kinesisvideosignaling#IceServerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_signaling.types.ice_server

IceServerList: TypeAlias = list[
    "aws_sdk_kinesis_video_signaling.types.ice_server.IceServer"
]


# --- restJson1 ser/de ---
def serialize_json(value: IceServerList) -> list:
    import aws_sdk_kinesis_video_signaling.types.ice_server

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_video_signaling.types.ice_server.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IceServerList:
    import aws_sdk_kinesis_video_signaling.types.ice_server

    out: IceServerList = []
    for item in data:
        out.append(
            aws_sdk_kinesis_video_signaling.types.ice_server.deserialize_json(item)
        )
    return out
