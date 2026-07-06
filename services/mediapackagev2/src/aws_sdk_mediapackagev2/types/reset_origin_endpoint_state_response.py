"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ResetOriginEndpointStateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mediapackagev2.types.resource_name


class ResetOriginEndpointStateResponse(TypedDict, closed=True):
    channel_group_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the channel group that contains the channel with the origin endpoint that you just reset.</p>"""
    channel_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the channel with the origin endpoint that you just reset.</p>"""
    origin_endpoint_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the origin endpoint that you just reset.</p>"""
    arn: "str"
    """<p>The Amazon Resource Name (ARN) associated with the endpoint that you just reset.</p>"""
    reset_at: "datetime.datetime"
    """<p>The time that the origin endpoint was last reset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetOriginEndpointStateResponse) -> dict:
    out: dict = {}
    out["ChannelGroupName"] = value["channel_group_name"]
    out["ChannelName"] = value["channel_name"]
    out["OriginEndpointName"] = value["origin_endpoint_name"]
    out["Arn"] = value["arn"]
    import aws_sdk_mediapackagev2.types._prelude.timestamp

    out["ResetAt"] = aws_sdk_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["reset_at"]
    )
    return out


def deserialize_json(data: dict) -> ResetOriginEndpointStateResponse:
    out: ResetOriginEndpointStateResponse = {}  # type: ignore[typeddict-item]
    if "ChannelGroupName" in data:
        out["channel_group_name"] = data["ChannelGroupName"]
    else:
        raise DeserializationError(
            "ResetOriginEndpointStateResponse.channel_group_name required"
        )
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    else:
        raise DeserializationError(
            "ResetOriginEndpointStateResponse.channel_name required"
        )
    if "OriginEndpointName" in data:
        out["origin_endpoint_name"] = data["OriginEndpointName"]
    else:
        raise DeserializationError(
            "ResetOriginEndpointStateResponse.origin_endpoint_name required"
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ResetOriginEndpointStateResponse.arn required")
    if "ResetAt" in data:
        import aws_sdk_mediapackagev2.types._prelude.timestamp

        out["reset_at"] = (
            aws_sdk_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["ResetAt"]
            )
        )
    else:
        raise DeserializationError("ResetOriginEndpointStateResponse.reset_at required")
    return out
