"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#UpdateSignalingChannelInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.resource_arn
    import aws_sdk_kinesis_video.types.single_master_configuration
    import aws_sdk_kinesis_video.types.version


class UpdateSignalingChannelInput(TypedDict):
    channel_arn: "aws_sdk_kinesis_video.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the signaling channel that you want to update.</p>"""
    current_version: "aws_sdk_kinesis_video.types.version.Version"
    """<p>The current version of the signaling channel that you want to update.</p>"""
    single_master_configuration: NotRequired[
        "aws_sdk_kinesis_video.types.single_master_configuration.SingleMasterConfiguration"
    ]
    """<p>The structure containing the configuration for the <code>SINGLE_MASTER</code> type of the signaling channel that you want to update. This parameter and the channel message's time-to-live are required for channels with the <code>SINGLE_MASTER</code> channel type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSignalingChannelInput) -> dict:
    out: dict = {}
    out["ChannelARN"] = value["channel_arn"]
    out["CurrentVersion"] = value["current_version"]
    if "single_master_configuration" in value:
        import aws_sdk_kinesis_video.types.single_master_configuration

        out["SingleMasterConfiguration"] = (
            aws_sdk_kinesis_video.types.single_master_configuration.serialize_json(
                value["single_master_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSignalingChannelInput:
    out: UpdateSignalingChannelInput = {}  # type: ignore[typeddict-item]
    if "ChannelARN" in data:
        out["channel_arn"] = data["ChannelARN"]
    else:
        raise DeserializationError("UpdateSignalingChannelInput.channel_arn required")
    if "CurrentVersion" in data:
        out["current_version"] = data["CurrentVersion"]
    else:
        raise DeserializationError(
            "UpdateSignalingChannelInput.current_version required"
        )
    if "SingleMasterConfiguration" in data:
        import aws_sdk_kinesis_video.types.single_master_configuration

        out["single_master_configuration"] = (
            aws_sdk_kinesis_video.types.single_master_configuration.deserialize_json(
                data["SingleMasterConfiguration"]
            )
        )
    return out
