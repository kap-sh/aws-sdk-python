"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddFlowMediaStreamsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_add_media_stream_request
    import aws_sdk_mediaconnect.types.flow_arn


class AddFlowMediaStreamsRequest(TypedDict, closed=True):
    flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn"
    """<p> The Amazon Resource Name (ARN) of the flow.</p>"""
    media_streams: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_add_media_stream_request.__listOfAddMediaStreamRequest"
    ]
    """<p> The media streams that you want to add to the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddFlowMediaStreamsRequest) -> dict:
    out: dict = {}
    if "media_streams" in value:
        import aws_sdk_mediaconnect.types.__list_of_add_media_stream_request

        out["mediaStreams"] = (
            aws_sdk_mediaconnect.types.__list_of_add_media_stream_request.serialize_json(
                value["media_streams"]
            )
        )
    return out


def deserialize_json(data: dict) -> AddFlowMediaStreamsRequest:
    out: AddFlowMediaStreamsRequest = {}  # type: ignore[typeddict-item]
    if "mediaStreams" in data:
        import aws_sdk_mediaconnect.types.__list_of_add_media_stream_request

        out["media_streams"] = (
            aws_sdk_mediaconnect.types.__list_of_add_media_stream_request.deserialize_json(
                data["mediaStreams"]
            )
        )
    return out
