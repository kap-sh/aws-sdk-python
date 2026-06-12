"""Generated from Smithy shape ``com.amazonaws.ivs#BatchStartViewerSessionRevocationError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.channel_arn
    import aws_sdk_ivs.types.error_code
    import aws_sdk_ivs.types.error_message
    import aws_sdk_ivs.types.viewer_id


class BatchStartViewerSessionRevocationError(TypedDict):
    channel_arn: "aws_sdk_ivs.types.channel_arn.ChannelArn"
    """<p>Channel ARN.</p>"""
    viewer_id: "aws_sdk_ivs.types.viewer_id.ViewerId"
    """<p>The ID of the viewer session to revoke.</p>"""
    code: NotRequired["aws_sdk_ivs.types.error_code.errorCode"]
    """<p>Error code.</p>"""
    message: NotRequired["aws_sdk_ivs.types.error_message.errorMessage"]
    """<p>Error message, determined by the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchStartViewerSessionRevocationError) -> dict:
    out: dict = {}
    out["channelArn"] = value["channel_arn"]
    out["viewerId"] = value["viewer_id"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchStartViewerSessionRevocationError:
    out: BatchStartViewerSessionRevocationError = {}  # type: ignore[typeddict-item]
    if "channelArn" in data:
        out["channel_arn"] = data["channelArn"]
    else:
        raise DeserializationError(
            "BatchStartViewerSessionRevocationError.channel_arn required"
        )
    if "viewerId" in data:
        out["viewer_id"] = data["viewerId"]
    else:
        raise DeserializationError(
            "BatchStartViewerSessionRevocationError.viewer_id required"
        )
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out
