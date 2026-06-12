"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#GetSignalingChannelEndpointInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.resource_arn
    import aws_sdk_kinesis_video.types.single_master_channel_endpoint_configuration


class GetSignalingChannelEndpointInput(TypedDict):
    channel_arn: "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the signalling channel for which you want to get an endpoint.</p>"""
    single_master_channel_endpoint_configuration: NotRequired[
        "aws_sdk_kinesis_video.types.single_master_channel_endpoint_configuration.SingleMasterChannelEndpointConfiguration"
    ]
    """<p>A structure containing the endpoint configuration for the <code>SINGLE_MASTER</code> channel type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSignalingChannelEndpointInput) -> dict:
    out: dict = {}
    out["ChannelARN"] = value["channel_arn"]
    if "single_master_channel_endpoint_configuration" in value:
        import aws_sdk_kinesis_video.types.single_master_channel_endpoint_configuration

        out["SingleMasterChannelEndpointConfiguration"] = (
            aws_sdk_kinesis_video.types.single_master_channel_endpoint_configuration.serialize_json(
                value["single_master_channel_endpoint_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSignalingChannelEndpointInput:
    out: GetSignalingChannelEndpointInput = {}  # type: ignore[typeddict-item]
    if "ChannelARN" in data:
        out["channel_arn"] = data["ChannelARN"]
    else:
        raise DeserializationError(
            "GetSignalingChannelEndpointInput.channel_arn required"
        )
    if "SingleMasterChannelEndpointConfiguration" in data:
        import aws_sdk_kinesis_video.types.single_master_channel_endpoint_configuration

        out["single_master_channel_endpoint_configuration"] = (
            aws_sdk_kinesis_video.types.single_master_channel_endpoint_configuration.deserialize_json(
                data["SingleMasterChannelEndpointConfiguration"]
            )
        )
    return out
