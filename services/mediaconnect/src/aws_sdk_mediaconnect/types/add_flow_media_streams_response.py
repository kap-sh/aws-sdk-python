"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddFlowMediaStreamsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_media_stream


class AddFlowMediaStreamsResponse(TypedDict, closed=True):
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that you added media streams to.</p>"""
    media_streams: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_media_stream.__listOfMediaStream"
    ]
    """<p> The media streams that you added to the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddFlowMediaStreamsResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "media_streams" in value:
        import aws_sdk_mediaconnect.types.__list_of_media_stream

        out["mediaStreams"] = (
            aws_sdk_mediaconnect.types.__list_of_media_stream.serialize_json(
                value["media_streams"]
            )
        )
    return out


def deserialize_json(data: dict) -> AddFlowMediaStreamsResponse:
    out: AddFlowMediaStreamsResponse = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "mediaStreams" in data:
        import aws_sdk_mediaconnect.types.__list_of_media_stream

        out["media_streams"] = (
            aws_sdk_mediaconnect.types.__list_of_media_stream.deserialize_json(
                data["mediaStreams"]
            )
        )
    return out
