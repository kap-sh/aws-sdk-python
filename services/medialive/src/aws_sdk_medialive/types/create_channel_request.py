"""Generated from Smithy shape ``com.amazonaws.medialive#CreateChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__boolean
    import aws_sdk_medialive.types.__list_of__string
    import aws_sdk_medialive.types.__list_of_input_attachment
    import aws_sdk_medialive.types.__list_of_output_destination
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.anywhere_settings
    import aws_sdk_medialive.types.cdi_input_specification
    import aws_sdk_medialive.types.channel_class
    import aws_sdk_medialive.types.channel_engine_version_request
    import aws_sdk_medialive.types.encoder_settings
    import aws_sdk_medialive.types.inference_settings
    import aws_sdk_medialive.types.input_specification
    import aws_sdk_medialive.types.linked_channel_settings
    import aws_sdk_medialive.types.log_level
    import aws_sdk_medialive.types.maintenance_create_settings
    import aws_sdk_medialive.types.tags
    import aws_sdk_medialive.types.vpc_output_settings


class CreateChannelRequest(TypedDict, closed=True):
    cdi_input_specification: NotRequired[
        "aws_sdk_medialive.types.cdi_input_specification.CdiInputSpecification"
    ]
    """Specification of CDI inputs for this channel"""
    channel_class: NotRequired["aws_sdk_medialive.types.channel_class.ChannelClass"]
    """The class for this channel. STANDARD for a channel with two pipelines or SINGLE_PIPELINE for a channel with one pipeline."""
    destinations: NotRequired[
        "aws_sdk_medialive.types.__list_of_output_destination.__listOfOutputDestination"
    ]
    encoder_settings: NotRequired[
        "aws_sdk_medialive.types.encoder_settings.EncoderSettings"
    ]
    input_attachments: NotRequired[
        "aws_sdk_medialive.types.__list_of_input_attachment.__listOfInputAttachment"
    ]
    """List of input attachments for channel."""
    input_specification: NotRequired[
        "aws_sdk_medialive.types.input_specification.InputSpecification"
    ]
    """Specification of network and file inputs for this channel"""
    log_level: NotRequired["aws_sdk_medialive.types.log_level.LogLevel"]
    """The log level to write to CloudWatch Logs."""
    maintenance: NotRequired[
        "aws_sdk_medialive.types.maintenance_create_settings.MaintenanceCreateSettings"
    ]
    """Maintenance settings for this channel."""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Name of channel."""
    request_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Unique request ID to be specified. This is needed to prevent retries from creating multiple resources."""
    reserved: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Deprecated field that's only usable by whitelisted customers."""
    role_arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """An optional Amazon Resource Name (ARN) of the role to assume when running the Channel."""
    tags: NotRequired["aws_sdk_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""
    vpc: NotRequired["aws_sdk_medialive.types.vpc_output_settings.VpcOutputSettings"]
    """Settings for the VPC outputs"""
    anywhere_settings: NotRequired[
        "aws_sdk_medialive.types.anywhere_settings.AnywhereSettings"
    ]
    """The Elemental Anywhere settings for this channel."""
    channel_engine_version: NotRequired[
        "aws_sdk_medialive.types.channel_engine_version_request.ChannelEngineVersionRequest"
    ]
    """The desired engine version for this channel."""
    dry_run: NotRequired["aws_sdk_medialive.types.__boolean.__boolean"]
    linked_channel_settings: NotRequired[
        "aws_sdk_medialive.types.linked_channel_settings.LinkedChannelSettings"
    ]
    """The linked channel settings for the channel."""
    channel_security_groups: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """A list of IDs for all the Input Security Groups attached to the channel."""
    inference_settings: NotRequired[
        "aws_sdk_medialive.types.inference_settings.InferenceSettings"
    ]
    """Include this setting to include Elemental Inference features in this channel."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelRequest) -> dict:
    out: dict = {}
    if "cdi_input_specification" in value:
        import aws_sdk_medialive.types.cdi_input_specification

        out["cdiInputSpecification"] = (
            aws_sdk_medialive.types.cdi_input_specification.serialize_json(
                value["cdi_input_specification"]
            )
        )
    if "channel_class" in value:
        import aws_sdk_medialive.types.channel_class

        out["channelClass"] = aws_sdk_medialive.types.channel_class.serialize_json(
            value["channel_class"]
        )
    if "destinations" in value:
        import aws_sdk_medialive.types.__list_of_output_destination

        out["destinations"] = (
            aws_sdk_medialive.types.__list_of_output_destination.serialize_json(
                value["destinations"]
            )
        )
    if "encoder_settings" in value:
        import aws_sdk_medialive.types.encoder_settings

        out["encoderSettings"] = (
            aws_sdk_medialive.types.encoder_settings.serialize_json(
                value["encoder_settings"]
            )
        )
    if "input_attachments" in value:
        import aws_sdk_medialive.types.__list_of_input_attachment

        out["inputAttachments"] = (
            aws_sdk_medialive.types.__list_of_input_attachment.serialize_json(
                value["input_attachments"]
            )
        )
    if "input_specification" in value:
        import aws_sdk_medialive.types.input_specification

        out["inputSpecification"] = (
            aws_sdk_medialive.types.input_specification.serialize_json(
                value["input_specification"]
            )
        )
    if "log_level" in value:
        import aws_sdk_medialive.types.log_level

        out["logLevel"] = aws_sdk_medialive.types.log_level.serialize_json(
            value["log_level"]
        )
    if "maintenance" in value:
        import aws_sdk_medialive.types.maintenance_create_settings

        out["maintenance"] = (
            aws_sdk_medialive.types.maintenance_create_settings.serialize_json(
                value["maintenance"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "reserved" in value:
        out["reserved"] = value["reserved"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.serialize_json(value["tags"])
    if "vpc" in value:
        import aws_sdk_medialive.types.vpc_output_settings

        out["vpc"] = aws_sdk_medialive.types.vpc_output_settings.serialize_json(
            value["vpc"]
        )
    if "anywhere_settings" in value:
        import aws_sdk_medialive.types.anywhere_settings

        out["anywhereSettings"] = (
            aws_sdk_medialive.types.anywhere_settings.serialize_json(
                value["anywhere_settings"]
            )
        )
    if "channel_engine_version" in value:
        import aws_sdk_medialive.types.channel_engine_version_request

        out["channelEngineVersion"] = (
            aws_sdk_medialive.types.channel_engine_version_request.serialize_json(
                value["channel_engine_version"]
            )
        )
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    if "linked_channel_settings" in value:
        import aws_sdk_medialive.types.linked_channel_settings

        out["linkedChannelSettings"] = (
            aws_sdk_medialive.types.linked_channel_settings.serialize_json(
                value["linked_channel_settings"]
            )
        )
    if "channel_security_groups" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["channelSecurityGroups"] = (
            aws_sdk_medialive.types.__list_of__string.serialize_json(
                value["channel_security_groups"]
            )
        )
    if "inference_settings" in value:
        import aws_sdk_medialive.types.inference_settings

        out["inferenceSettings"] = (
            aws_sdk_medialive.types.inference_settings.serialize_json(
                value["inference_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateChannelRequest:
    out: CreateChannelRequest = {}  # type: ignore[typeddict-item]
    if "cdiInputSpecification" in data:
        import aws_sdk_medialive.types.cdi_input_specification

        out["cdi_input_specification"] = (
            aws_sdk_medialive.types.cdi_input_specification.deserialize_json(
                data["cdiInputSpecification"]
            )
        )
    if "channelClass" in data:
        import aws_sdk_medialive.types.channel_class

        out["channel_class"] = aws_sdk_medialive.types.channel_class.deserialize_json(
            data["channelClass"]
        )
    if "destinations" in data:
        import aws_sdk_medialive.types.__list_of_output_destination

        out["destinations"] = (
            aws_sdk_medialive.types.__list_of_output_destination.deserialize_json(
                data["destinations"]
            )
        )
    if "encoderSettings" in data:
        import aws_sdk_medialive.types.encoder_settings

        out["encoder_settings"] = (
            aws_sdk_medialive.types.encoder_settings.deserialize_json(
                data["encoderSettings"]
            )
        )
    if "inputAttachments" in data:
        import aws_sdk_medialive.types.__list_of_input_attachment

        out["input_attachments"] = (
            aws_sdk_medialive.types.__list_of_input_attachment.deserialize_json(
                data["inputAttachments"]
            )
        )
    if "inputSpecification" in data:
        import aws_sdk_medialive.types.input_specification

        out["input_specification"] = (
            aws_sdk_medialive.types.input_specification.deserialize_json(
                data["inputSpecification"]
            )
        )
    if "logLevel" in data:
        import aws_sdk_medialive.types.log_level

        out["log_level"] = aws_sdk_medialive.types.log_level.deserialize_json(
            data["logLevel"]
        )
    if "maintenance" in data:
        import aws_sdk_medialive.types.maintenance_create_settings

        out["maintenance"] = (
            aws_sdk_medialive.types.maintenance_create_settings.deserialize_json(
                data["maintenance"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "reserved" in data:
        out["reserved"] = data["reserved"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "tags" in data:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.deserialize_json(data["tags"])
    if "vpc" in data:
        import aws_sdk_medialive.types.vpc_output_settings

        out["vpc"] = aws_sdk_medialive.types.vpc_output_settings.deserialize_json(
            data["vpc"]
        )
    if "anywhereSettings" in data:
        import aws_sdk_medialive.types.anywhere_settings

        out["anywhere_settings"] = (
            aws_sdk_medialive.types.anywhere_settings.deserialize_json(
                data["anywhereSettings"]
            )
        )
    if "channelEngineVersion" in data:
        import aws_sdk_medialive.types.channel_engine_version_request

        out["channel_engine_version"] = (
            aws_sdk_medialive.types.channel_engine_version_request.deserialize_json(
                data["channelEngineVersion"]
            )
        )
    if "dryRun" in data:
        out["dry_run"] = data["dryRun"]
    if "linkedChannelSettings" in data:
        import aws_sdk_medialive.types.linked_channel_settings

        out["linked_channel_settings"] = (
            aws_sdk_medialive.types.linked_channel_settings.deserialize_json(
                data["linkedChannelSettings"]
            )
        )
    if "channelSecurityGroups" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["channel_security_groups"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["channelSecurityGroups"]
            )
        )
    if "inferenceSettings" in data:
        import aws_sdk_medialive.types.inference_settings

        out["inference_settings"] = (
            aws_sdk_medialive.types.inference_settings.deserialize_json(
                data["inferenceSettings"]
            )
        )
    return out
