"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#OutboundRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.channel_subtype_parameters
    import aws_sdk_connectcampaignsv2.types.client_token
    import aws_sdk_connectcampaignsv2.types.time_stamp


class OutboundRequest(TypedDict):
    client_token: "aws_sdk_connectcampaignsv2.types.client_token.ClientToken"
    expiration_time: "aws_sdk_connectcampaignsv2.types.time_stamp.TimeStamp"
    channel_subtype_parameters: "aws_sdk_connectcampaignsv2.types.channel_subtype_parameters.ChannelSubtypeParameters"


# --- restJson1 ser/de ---
def serialize_json(value: OutboundRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    import aws_sdk_connectcampaignsv2.types.time_stamp

    out["expirationTime"] = aws_sdk_connectcampaignsv2.types.time_stamp.serialize_json(
        value["expiration_time"]
    )
    import aws_sdk_connectcampaignsv2.types.channel_subtype_parameters

    out["channelSubtypeParameters"] = (
        aws_sdk_connectcampaignsv2.types.channel_subtype_parameters.serialize_json(
            value["channel_subtype_parameters"]
        )
    )
    return out


def deserialize_json(data: dict) -> OutboundRequest:
    out: OutboundRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("OutboundRequest.client_token required")
    if "expirationTime" in data:
        import aws_sdk_connectcampaignsv2.types.time_stamp

        out["expiration_time"] = (
            aws_sdk_connectcampaignsv2.types.time_stamp.deserialize_json(
                data["expirationTime"]
            )
        )
    else:
        raise DeserializationError("OutboundRequest.expiration_time required")
    if "channelSubtypeParameters" in data:
        import aws_sdk_connectcampaignsv2.types.channel_subtype_parameters

        out["channel_subtype_parameters"] = (
            aws_sdk_connectcampaignsv2.types.channel_subtype_parameters.deserialize_json(
                data["channelSubtypeParameters"]
            )
        )
    else:
        raise DeserializationError(
            "OutboundRequest.channel_subtype_parameters required"
        )
    return out
