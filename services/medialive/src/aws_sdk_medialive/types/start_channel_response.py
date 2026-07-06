"""Generated from Smithy shape ``com.amazonaws.medialive#StartChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer
    import aws_sdk_medialive.types.__list_of__string
    import aws_sdk_medialive.types.__list_of_channel_egress_endpoint
    import aws_sdk_medialive.types.__list_of_input_attachment
    import aws_sdk_medialive.types.__list_of_output_destination
    import aws_sdk_medialive.types.__list_of_pipeline_detail
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.cdi_input_specification
    import aws_sdk_medialive.types.channel_class
    import aws_sdk_medialive.types.channel_engine_version_response
    import aws_sdk_medialive.types.channel_state
    import aws_sdk_medialive.types.describe_anywhere_settings
    import aws_sdk_medialive.types.describe_inference_settings
    import aws_sdk_medialive.types.describe_linked_channel_settings
    import aws_sdk_medialive.types.encoder_settings
    import aws_sdk_medialive.types.input_specification
    import aws_sdk_medialive.types.log_level
    import aws_sdk_medialive.types.maintenance_status
    import aws_sdk_medialive.types.tags
    import aws_sdk_medialive.types.vpc_output_settings_description


class StartChannelResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The unique arn of the channel."""
    cdi_input_specification: NotRequired[
        "aws_sdk_medialive.types.cdi_input_specification.CdiInputSpecification"
    ]
    """Specification of CDI inputs for this channel"""
    channel_class: NotRequired["aws_sdk_medialive.types.channel_class.ChannelClass"]
    """The class for this channel. STANDARD for a channel with two pipelines or SINGLE_PIPELINE for a channel with one pipeline."""
    destinations: NotRequired[
        "aws_sdk_medialive.types.__list_of_output_destination.__listOfOutputDestination"
    ]
    """A list of destinations of the channel. For UDP outputs, there is one destination per output. For other types (HLS, for example), there is one destination per packager."""
    egress_endpoints: NotRequired[
        "aws_sdk_medialive.types.__list_of_channel_egress_endpoint.__listOfChannelEgressEndpoint"
    ]
    """The endpoints where outgoing connections initiate from"""
    encoder_settings: NotRequired[
        "aws_sdk_medialive.types.encoder_settings.EncoderSettings"
    ]
    id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The unique id of the channel."""
    input_attachments: NotRequired[
        "aws_sdk_medialive.types.__list_of_input_attachment.__listOfInputAttachment"
    ]
    """List of input attachments for channel."""
    input_specification: NotRequired[
        "aws_sdk_medialive.types.input_specification.InputSpecification"
    ]
    """Specification of network and file inputs for this channel"""
    log_level: NotRequired["aws_sdk_medialive.types.log_level.LogLevel"]
    """The log level being written to CloudWatch Logs."""
    maintenance: NotRequired[
        "aws_sdk_medialive.types.maintenance_status.MaintenanceStatus"
    ]
    """Maintenance settings for this channel."""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The name of the channel. (user-mutable)"""
    pipeline_details: NotRequired[
        "aws_sdk_medialive.types.__list_of_pipeline_detail.__listOfPipelineDetail"
    ]
    """Runtime details for the pipelines of a running channel."""
    pipelines_running_count: NotRequired["aws_sdk_medialive.types.__integer.__integer"]
    """The number of currently healthy pipelines."""
    role_arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The Amazon Resource Name (ARN) of the role assumed when running the Channel."""
    state: NotRequired["aws_sdk_medialive.types.channel_state.ChannelState"]
    tags: NotRequired["aws_sdk_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""
    vpc: NotRequired[
        "aws_sdk_medialive.types.vpc_output_settings_description.VpcOutputSettingsDescription"
    ]
    """Settings for VPC output"""
    anywhere_settings: NotRequired[
        "aws_sdk_medialive.types.describe_anywhere_settings.DescribeAnywhereSettings"
    ]
    """Anywhere settings for this channel."""
    channel_engine_version: NotRequired[
        "aws_sdk_medialive.types.channel_engine_version_response.ChannelEngineVersionResponse"
    ]
    """Requested engine version for this channel."""
    linked_channel_settings: NotRequired[
        "aws_sdk_medialive.types.describe_linked_channel_settings.DescribeLinkedChannelSettings"
    ]
    """Linked Channel Settings for this channel."""
    channel_security_groups: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """A list of IDs for all the Input Security Groups attached to the channel."""
    inference_settings: NotRequired[
        "aws_sdk_medialive.types.describe_inference_settings.DescribeInferenceSettings"
    ]
    """Include this setting to include Elemental Inference features in this channel."""


# --- restJson1 ser/de ---
def serialize_json(value: StartChannelResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
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
    if "egress_endpoints" in value:
        import aws_sdk_medialive.types.__list_of_channel_egress_endpoint

        out["egressEndpoints"] = (
            aws_sdk_medialive.types.__list_of_channel_egress_endpoint.serialize_json(
                value["egress_endpoints"]
            )
        )
    if "encoder_settings" in value:
        import aws_sdk_medialive.types.encoder_settings

        out["encoderSettings"] = (
            aws_sdk_medialive.types.encoder_settings.serialize_json(
                value["encoder_settings"]
            )
        )
    if "id" in value:
        out["id"] = value["id"]
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
        import aws_sdk_medialive.types.maintenance_status

        out["maintenance"] = aws_sdk_medialive.types.maintenance_status.serialize_json(
            value["maintenance"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "pipeline_details" in value:
        import aws_sdk_medialive.types.__list_of_pipeline_detail

        out["pipelineDetails"] = (
            aws_sdk_medialive.types.__list_of_pipeline_detail.serialize_json(
                value["pipeline_details"]
            )
        )
    if "pipelines_running_count" in value:
        out["pipelinesRunningCount"] = value["pipelines_running_count"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "state" in value:
        import aws_sdk_medialive.types.channel_state

        out["state"] = aws_sdk_medialive.types.channel_state.serialize_json(
            value["state"]
        )
    if "tags" in value:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.serialize_json(value["tags"])
    if "vpc" in value:
        import aws_sdk_medialive.types.vpc_output_settings_description

        out["vpc"] = (
            aws_sdk_medialive.types.vpc_output_settings_description.serialize_json(
                value["vpc"]
            )
        )
    if "anywhere_settings" in value:
        import aws_sdk_medialive.types.describe_anywhere_settings

        out["anywhereSettings"] = (
            aws_sdk_medialive.types.describe_anywhere_settings.serialize_json(
                value["anywhere_settings"]
            )
        )
    if "channel_engine_version" in value:
        import aws_sdk_medialive.types.channel_engine_version_response

        out["channelEngineVersion"] = (
            aws_sdk_medialive.types.channel_engine_version_response.serialize_json(
                value["channel_engine_version"]
            )
        )
    if "linked_channel_settings" in value:
        import aws_sdk_medialive.types.describe_linked_channel_settings

        out["linkedChannelSettings"] = (
            aws_sdk_medialive.types.describe_linked_channel_settings.serialize_json(
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
        import aws_sdk_medialive.types.describe_inference_settings

        out["inferenceSettings"] = (
            aws_sdk_medialive.types.describe_inference_settings.serialize_json(
                value["inference_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartChannelResponse:
    out: StartChannelResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
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
    if "egressEndpoints" in data:
        import aws_sdk_medialive.types.__list_of_channel_egress_endpoint

        out["egress_endpoints"] = (
            aws_sdk_medialive.types.__list_of_channel_egress_endpoint.deserialize_json(
                data["egressEndpoints"]
            )
        )
    if "encoderSettings" in data:
        import aws_sdk_medialive.types.encoder_settings

        out["encoder_settings"] = (
            aws_sdk_medialive.types.encoder_settings.deserialize_json(
                data["encoderSettings"]
            )
        )
    if "id" in data:
        out["id"] = data["id"]
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
        import aws_sdk_medialive.types.maintenance_status

        out["maintenance"] = (
            aws_sdk_medialive.types.maintenance_status.deserialize_json(
                data["maintenance"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "pipelineDetails" in data:
        import aws_sdk_medialive.types.__list_of_pipeline_detail

        out["pipeline_details"] = (
            aws_sdk_medialive.types.__list_of_pipeline_detail.deserialize_json(
                data["pipelineDetails"]
            )
        )
    if "pipelinesRunningCount" in data:
        out["pipelines_running_count"] = data["pipelinesRunningCount"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "state" in data:
        import aws_sdk_medialive.types.channel_state

        out["state"] = aws_sdk_medialive.types.channel_state.deserialize_json(
            data["state"]
        )
    if "tags" in data:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.deserialize_json(data["tags"])
    if "vpc" in data:
        import aws_sdk_medialive.types.vpc_output_settings_description

        out["vpc"] = (
            aws_sdk_medialive.types.vpc_output_settings_description.deserialize_json(
                data["vpc"]
            )
        )
    if "anywhereSettings" in data:
        import aws_sdk_medialive.types.describe_anywhere_settings

        out["anywhere_settings"] = (
            aws_sdk_medialive.types.describe_anywhere_settings.deserialize_json(
                data["anywhereSettings"]
            )
        )
    if "channelEngineVersion" in data:
        import aws_sdk_medialive.types.channel_engine_version_response

        out["channel_engine_version"] = (
            aws_sdk_medialive.types.channel_engine_version_response.deserialize_json(
                data["channelEngineVersion"]
            )
        )
    if "linkedChannelSettings" in data:
        import aws_sdk_medialive.types.describe_linked_channel_settings

        out["linked_channel_settings"] = (
            aws_sdk_medialive.types.describe_linked_channel_settings.deserialize_json(
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
        import aws_sdk_medialive.types.describe_inference_settings

        out["inference_settings"] = (
            aws_sdk_medialive.types.describe_inference_settings.deserialize_json(
                data["inferenceSettings"]
            )
        )
    return out
