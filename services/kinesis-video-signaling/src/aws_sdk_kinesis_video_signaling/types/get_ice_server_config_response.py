"""Generated from Smithy shape ``com.amazonaws.kinesisvideosignaling#GetIceServerConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_signaling.types.ice_server_list


class GetIceServerConfigResponse(TypedDict, closed=True):
    ice_server_list: NotRequired[
        "aws_sdk_kinesis_video_signaling.types.ice_server_list.IceServerList"
    ]
    """<p>The list of ICE server information objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIceServerConfigResponse) -> dict:
    out: dict = {}
    if "ice_server_list" in value:
        import aws_sdk_kinesis_video_signaling.types.ice_server_list

        out["IceServerList"] = (
            aws_sdk_kinesis_video_signaling.types.ice_server_list.serialize_json(
                value["ice_server_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetIceServerConfigResponse:
    out: GetIceServerConfigResponse = {}  # type: ignore[typeddict-item]
    if "IceServerList" in data:
        import aws_sdk_kinesis_video_signaling.types.ice_server_list

        out["ice_server_list"] = (
            aws_sdk_kinesis_video_signaling.types.ice_server_list.deserialize_json(
                data["IceServerList"]
            )
        )
    return out
