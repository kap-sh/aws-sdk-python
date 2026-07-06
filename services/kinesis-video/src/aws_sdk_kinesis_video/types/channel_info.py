"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ChannelInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.channel_name
    import aws_sdk_kinesis_video.types.channel_type
    import aws_sdk_kinesis_video.types.resource_arn
    import aws_sdk_kinesis_video.types.single_master_configuration
    import aws_sdk_kinesis_video.types.status
    import aws_sdk_kinesis_video.types.timestamp
    import aws_sdk_kinesis_video.types.version


class ChannelInfo(TypedDict, closed=True):
    channel_name: NotRequired["aws_sdk_kinesis_video.types.channel_name.ChannelName"]
    """<p>The name of the signaling channel.</p>"""
    channel_arn: NotRequired["aws_sdk_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the signaling channel.</p>"""
    channel_type: NotRequired["aws_sdk_kinesis_video.types.channel_type.ChannelType"]
    """<p>The type of the signaling channel.</p>"""
    channel_status: NotRequired["aws_sdk_kinesis_video.types.status.Status"]
    """<p>Current status of the signaling channel.</p>"""
    creation_time: NotRequired["aws_sdk_kinesis_video.types.timestamp.Timestamp"]
    """<p>The time at which the signaling channel was created.</p>"""
    single_master_configuration: NotRequired[
        "aws_sdk_kinesis_video.types.single_master_configuration.SingleMasterConfiguration"
    ]
    """<p>A structure that contains the configuration for the <code>SINGLE_MASTER</code> channel type.</p>"""
    version: NotRequired["aws_sdk_kinesis_video.types.version.Version"]
    """<p>The current version of the signaling channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelInfo) -> dict:
    out: dict = {}
    if "channel_name" in value:
        out["ChannelName"] = value["channel_name"]
    if "channel_arn" in value:
        out["ChannelARN"] = value["channel_arn"]
    if "channel_type" in value:
        import aws_sdk_kinesis_video.types.channel_type

        out["ChannelType"] = aws_sdk_kinesis_video.types.channel_type.serialize_json(
            value["channel_type"]
        )
    if "channel_status" in value:
        import aws_sdk_kinesis_video.types.status

        out["ChannelStatus"] = aws_sdk_kinesis_video.types.status.serialize_json(
            value["channel_status"]
        )
    if "creation_time" in value:
        import aws_sdk_kinesis_video.types.timestamp

        out["CreationTime"] = aws_sdk_kinesis_video.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "single_master_configuration" in value:
        import aws_sdk_kinesis_video.types.single_master_configuration

        out["SingleMasterConfiguration"] = (
            aws_sdk_kinesis_video.types.single_master_configuration.serialize_json(
                value["single_master_configuration"]
            )
        )
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> ChannelInfo:
    out: ChannelInfo = {}  # type: ignore[typeddict-item]
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    if "ChannelARN" in data:
        out["channel_arn"] = data["ChannelARN"]
    if "ChannelType" in data:
        import aws_sdk_kinesis_video.types.channel_type

        out["channel_type"] = aws_sdk_kinesis_video.types.channel_type.deserialize_json(
            data["ChannelType"]
        )
    if "ChannelStatus" in data:
        import aws_sdk_kinesis_video.types.status

        out["channel_status"] = aws_sdk_kinesis_video.types.status.deserialize_json(
            data["ChannelStatus"]
        )
    if "CreationTime" in data:
        import aws_sdk_kinesis_video.types.timestamp

        out["creation_time"] = aws_sdk_kinesis_video.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    if "SingleMasterConfiguration" in data:
        import aws_sdk_kinesis_video.types.single_master_configuration

        out["single_master_configuration"] = (
            aws_sdk_kinesis_video.types.single_master_configuration.deserialize_json(
                data["SingleMasterConfiguration"]
            )
        )
    if "Version" in data:
        out["version"] = data["Version"]
    return out
