"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#CreateSignalingChannelInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.channel_name
    import aws_sdk_kinesis_video.types.channel_type
    import aws_sdk_kinesis_video.types.single_master_configuration
    import aws_sdk_kinesis_video.types.tag_on_create_list


class CreateSignalingChannelInput(TypedDict):
    channel_name: "aws_sdk_kinesis_video.types.channel_name.ChannelName"
    """<p>A name for the signaling channel that you are creating. It must be unique for each Amazon Web Services account and Amazon Web Services Region.</p>"""
    channel_type: NotRequired["aws_sdk_kinesis_video.types.channel_type.ChannelType"]
    """<p>A type of the signaling channel that you are creating. Currently, <code>SINGLE_MASTER</code> is the only supported channel type. </p>"""
    single_master_configuration: NotRequired[
        "aws_sdk_kinesis_video.types.single_master_configuration.SingleMasterConfiguration"
    ]
    """<p>A structure containing the configuration for the <code>SINGLE_MASTER</code> channel type. The default configuration for the channel message's time to live is 60 seconds (1 minute).</p>"""
    tags: NotRequired["aws_sdk_kinesis_video.types.tag_on_create_list.TagOnCreateList"]
    """<p>A set of tags (key-value pairs) that you want to associate with this channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSignalingChannelInput) -> dict:
    out: dict = {}
    out["ChannelName"] = value["channel_name"]
    if "channel_type" in value:
        import aws_sdk_kinesis_video.types.channel_type

        out["ChannelType"] = aws_sdk_kinesis_video.types.channel_type.serialize_json(
            value["channel_type"]
        )
    if "single_master_configuration" in value:
        import aws_sdk_kinesis_video.types.single_master_configuration

        out["SingleMasterConfiguration"] = (
            aws_sdk_kinesis_video.types.single_master_configuration.serialize_json(
                value["single_master_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_kinesis_video.types.tag_on_create_list

        out["Tags"] = aws_sdk_kinesis_video.types.tag_on_create_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateSignalingChannelInput:
    out: CreateSignalingChannelInput = {}  # type: ignore[typeddict-item]
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    else:
        raise DeserializationError("CreateSignalingChannelInput.channel_name required")
    if "ChannelType" in data:
        import aws_sdk_kinesis_video.types.channel_type

        out["channel_type"] = aws_sdk_kinesis_video.types.channel_type.deserialize_json(
            data["ChannelType"]
        )
    if "SingleMasterConfiguration" in data:
        import aws_sdk_kinesis_video.types.single_master_configuration

        out["single_master_configuration"] = (
            aws_sdk_kinesis_video.types.single_master_configuration.deserialize_json(
                data["SingleMasterConfiguration"]
            )
        )
    if "Tags" in data:
        import aws_sdk_kinesis_video.types.tag_on_create_list

        out["tags"] = aws_sdk_kinesis_video.types.tag_on_create_list.deserialize_json(
            data["Tags"]
        )
    return out
