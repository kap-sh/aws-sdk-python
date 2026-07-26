"""Generated from Smithy shape ``com.amazonaws.medialive#StopChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer
    import capo_medialive.types.__list_of__string
    import capo_medialive.types.__list_of_channel_egress_endpoint
    import capo_medialive.types.__list_of_input_attachment
    import capo_medialive.types.__list_of_output_destination
    import capo_medialive.types.__list_of_pipeline_detail
    import capo_medialive.types.__string
    import capo_medialive.types.cdi_input_specification
    import capo_medialive.types.channel_class
    import capo_medialive.types.channel_engine_version_response
    import capo_medialive.types.channel_state
    import capo_medialive.types.describe_anywhere_settings
    import capo_medialive.types.describe_inference_settings
    import capo_medialive.types.describe_linked_channel_settings
    import capo_medialive.types.encoder_settings
    import capo_medialive.types.input_specification
    import capo_medialive.types.log_level
    import capo_medialive.types.maintenance_status
    import capo_medialive.types.tags
    import capo_medialive.types.vpc_output_settings_description


class StopChannelResponse(TypedDict, closed=True):
    arn: NotRequired["capo_medialive.types.__string.__string"]
    """The unique arn of the channel."""
    cdi_input_specification: NotRequired[
        "capo_medialive.types.cdi_input_specification.CdiInputSpecification"
    ]
    """Specification of CDI inputs for this channel"""
    channel_class: NotRequired["capo_medialive.types.channel_class.ChannelClass"]
    """The class for this channel. STANDARD for a channel with two pipelines or SINGLE_PIPELINE for a channel with one pipeline."""
    destinations: NotRequired[
        "capo_medialive.types.__list_of_output_destination.__listOfOutputDestination"
    ]
    """A list of destinations of the channel. For UDP outputs, there is one destination per output. For other types (HLS, for example), there is one destination per packager."""
    egress_endpoints: NotRequired[
        "capo_medialive.types.__list_of_channel_egress_endpoint.__listOfChannelEgressEndpoint"
    ]
    """The endpoints where outgoing connections initiate from"""
    encoder_settings: NotRequired[
        "capo_medialive.types.encoder_settings.EncoderSettings"
    ]
    id: NotRequired["capo_medialive.types.__string.__string"]
    """The unique id of the channel."""
    input_attachments: NotRequired[
        "capo_medialive.types.__list_of_input_attachment.__listOfInputAttachment"
    ]
    """List of input attachments for channel."""
    input_specification: NotRequired[
        "capo_medialive.types.input_specification.InputSpecification"
    ]
    """Specification of network and file inputs for this channel"""
    log_level: NotRequired["capo_medialive.types.log_level.LogLevel"]
    """The log level being written to CloudWatch Logs."""
    maintenance: NotRequired[
        "capo_medialive.types.maintenance_status.MaintenanceStatus"
    ]
    """Maintenance settings for this channel."""
    name: NotRequired["capo_medialive.types.__string.__string"]
    """The name of the channel. (user-mutable)"""
    pipeline_details: NotRequired[
        "capo_medialive.types.__list_of_pipeline_detail.__listOfPipelineDetail"
    ]
    """Runtime details for the pipelines of a running channel."""
    pipelines_running_count: NotRequired["capo_medialive.types.__integer.__integer"]
    """The number of currently healthy pipelines."""
    role_arn: NotRequired["capo_medialive.types.__string.__string"]
    """The Amazon Resource Name (ARN) of the role assumed when running the Channel."""
    state: NotRequired["capo_medialive.types.channel_state.ChannelState"]
    tags: NotRequired["capo_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""
    vpc: NotRequired[
        "capo_medialive.types.vpc_output_settings_description.VpcOutputSettingsDescription"
    ]
    """Settings for VPC output"""
    anywhere_settings: NotRequired[
        "capo_medialive.types.describe_anywhere_settings.DescribeAnywhereSettings"
    ]
    """Anywhere settings for this channel."""
    channel_engine_version: NotRequired[
        "capo_medialive.types.channel_engine_version_response.ChannelEngineVersionResponse"
    ]
    """Requested engine version for this channel."""
    linked_channel_settings: NotRequired[
        "capo_medialive.types.describe_linked_channel_settings.DescribeLinkedChannelSettings"
    ]
    """Linked Channel Settings for this channel."""
    channel_security_groups: NotRequired[
        "capo_medialive.types.__list_of__string.__listOf__string"
    ]
    """A list of IDs for all the Input Security Groups attached to the channel."""
    inference_settings: NotRequired[
        "capo_medialive.types.describe_inference_settings.DescribeInferenceSettings"
    ]
    """Include this setting to include Elemental Inference features in this channel."""


# --- restJson1 ser/de ---
def serialize_json(value: StopChannelResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "cdi_input_specification" in value:
        import capo_medialive.types.cdi_input_specification

        out["cdiInputSpecification"] = (
            capo_medialive.types.cdi_input_specification.serialize_json(
                value["cdi_input_specification"]
            )
        )
    if "channel_class" in value:
        import capo_medialive.types.channel_class

        out["channelClass"] = capo_medialive.types.channel_class.serialize_json(
            value["channel_class"]
        )
    if "destinations" in value:
        import capo_medialive.types.__list_of_output_destination

        out["destinations"] = (
            capo_medialive.types.__list_of_output_destination.serialize_json(
                value["destinations"]
            )
        )
    if "egress_endpoints" in value:
        import capo_medialive.types.__list_of_channel_egress_endpoint

        out["egressEndpoints"] = (
            capo_medialive.types.__list_of_channel_egress_endpoint.serialize_json(
                value["egress_endpoints"]
            )
        )
    if "encoder_settings" in value:
        import capo_medialive.types.encoder_settings

        out["encoderSettings"] = capo_medialive.types.encoder_settings.serialize_json(
            value["encoder_settings"]
        )
    if "id" in value:
        out["id"] = value["id"]
    if "input_attachments" in value:
        import capo_medialive.types.__list_of_input_attachment

        out["inputAttachments"] = (
            capo_medialive.types.__list_of_input_attachment.serialize_json(
                value["input_attachments"]
            )
        )
    if "input_specification" in value:
        import capo_medialive.types.input_specification

        out["inputSpecification"] = (
            capo_medialive.types.input_specification.serialize_json(
                value["input_specification"]
            )
        )
    if "log_level" in value:
        import capo_medialive.types.log_level

        out["logLevel"] = capo_medialive.types.log_level.serialize_json(
            value["log_level"]
        )
    if "maintenance" in value:
        import capo_medialive.types.maintenance_status

        out["maintenance"] = capo_medialive.types.maintenance_status.serialize_json(
            value["maintenance"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "pipeline_details" in value:
        import capo_medialive.types.__list_of_pipeline_detail

        out["pipelineDetails"] = (
            capo_medialive.types.__list_of_pipeline_detail.serialize_json(
                value["pipeline_details"]
            )
        )
    if "pipelines_running_count" in value:
        out["pipelinesRunningCount"] = value["pipelines_running_count"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "state" in value:
        import capo_medialive.types.channel_state

        out["state"] = capo_medialive.types.channel_state.serialize_json(value["state"])
    if "tags" in value:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.serialize_json(value["tags"])
    if "vpc" in value:
        import capo_medialive.types.vpc_output_settings_description

        out["vpc"] = (
            capo_medialive.types.vpc_output_settings_description.serialize_json(
                value["vpc"]
            )
        )
    if "anywhere_settings" in value:
        import capo_medialive.types.describe_anywhere_settings

        out["anywhereSettings"] = (
            capo_medialive.types.describe_anywhere_settings.serialize_json(
                value["anywhere_settings"]
            )
        )
    if "channel_engine_version" in value:
        import capo_medialive.types.channel_engine_version_response

        out["channelEngineVersion"] = (
            capo_medialive.types.channel_engine_version_response.serialize_json(
                value["channel_engine_version"]
            )
        )
    if "linked_channel_settings" in value:
        import capo_medialive.types.describe_linked_channel_settings

        out["linkedChannelSettings"] = (
            capo_medialive.types.describe_linked_channel_settings.serialize_json(
                value["linked_channel_settings"]
            )
        )
    if "channel_security_groups" in value:
        import capo_medialive.types.__list_of__string

        out["channelSecurityGroups"] = (
            capo_medialive.types.__list_of__string.serialize_json(
                value["channel_security_groups"]
            )
        )
    if "inference_settings" in value:
        import capo_medialive.types.describe_inference_settings

        out["inferenceSettings"] = (
            capo_medialive.types.describe_inference_settings.serialize_json(
                value["inference_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> StopChannelResponse:
    out: StopChannelResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "cdiInputSpecification" in data:
        import capo_medialive.types.cdi_input_specification

        out["cdi_input_specification"] = (
            capo_medialive.types.cdi_input_specification.deserialize_json(
                data["cdiInputSpecification"]
            )
        )
    if "channelClass" in data:
        import capo_medialive.types.channel_class

        out["channel_class"] = capo_medialive.types.channel_class.deserialize_json(
            data["channelClass"]
        )
    if "destinations" in data:
        import capo_medialive.types.__list_of_output_destination

        out["destinations"] = (
            capo_medialive.types.__list_of_output_destination.deserialize_json(
                data["destinations"]
            )
        )
    if "egressEndpoints" in data:
        import capo_medialive.types.__list_of_channel_egress_endpoint

        out["egress_endpoints"] = (
            capo_medialive.types.__list_of_channel_egress_endpoint.deserialize_json(
                data["egressEndpoints"]
            )
        )
    if "encoderSettings" in data:
        import capo_medialive.types.encoder_settings

        out["encoder_settings"] = (
            capo_medialive.types.encoder_settings.deserialize_json(
                data["encoderSettings"]
            )
        )
    if "id" in data:
        out["id"] = data["id"]
    if "inputAttachments" in data:
        import capo_medialive.types.__list_of_input_attachment

        out["input_attachments"] = (
            capo_medialive.types.__list_of_input_attachment.deserialize_json(
                data["inputAttachments"]
            )
        )
    if "inputSpecification" in data:
        import capo_medialive.types.input_specification

        out["input_specification"] = (
            capo_medialive.types.input_specification.deserialize_json(
                data["inputSpecification"]
            )
        )
    if "logLevel" in data:
        import capo_medialive.types.log_level

        out["log_level"] = capo_medialive.types.log_level.deserialize_json(
            data["logLevel"]
        )
    if "maintenance" in data:
        import capo_medialive.types.maintenance_status

        out["maintenance"] = capo_medialive.types.maintenance_status.deserialize_json(
            data["maintenance"]
        )
    if "name" in data:
        out["name"] = data["name"]
    if "pipelineDetails" in data:
        import capo_medialive.types.__list_of_pipeline_detail

        out["pipeline_details"] = (
            capo_medialive.types.__list_of_pipeline_detail.deserialize_json(
                data["pipelineDetails"]
            )
        )
    if "pipelinesRunningCount" in data:
        out["pipelines_running_count"] = data["pipelinesRunningCount"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "state" in data:
        import capo_medialive.types.channel_state

        out["state"] = capo_medialive.types.channel_state.deserialize_json(
            data["state"]
        )
    if "tags" in data:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.deserialize_json(data["tags"])
    if "vpc" in data:
        import capo_medialive.types.vpc_output_settings_description

        out["vpc"] = (
            capo_medialive.types.vpc_output_settings_description.deserialize_json(
                data["vpc"]
            )
        )
    if "anywhereSettings" in data:
        import capo_medialive.types.describe_anywhere_settings

        out["anywhere_settings"] = (
            capo_medialive.types.describe_anywhere_settings.deserialize_json(
                data["anywhereSettings"]
            )
        )
    if "channelEngineVersion" in data:
        import capo_medialive.types.channel_engine_version_response

        out["channel_engine_version"] = (
            capo_medialive.types.channel_engine_version_response.deserialize_json(
                data["channelEngineVersion"]
            )
        )
    if "linkedChannelSettings" in data:
        import capo_medialive.types.describe_linked_channel_settings

        out["linked_channel_settings"] = (
            capo_medialive.types.describe_linked_channel_settings.deserialize_json(
                data["linkedChannelSettings"]
            )
        )
    if "channelSecurityGroups" in data:
        import capo_medialive.types.__list_of__string

        out["channel_security_groups"] = (
            capo_medialive.types.__list_of__string.deserialize_json(
                data["channelSecurityGroups"]
            )
        )
    if "inferenceSettings" in data:
        import capo_medialive.types.describe_inference_settings

        out["inference_settings"] = (
            capo_medialive.types.describe_inference_settings.deserialize_json(
                data["inferenceSettings"]
            )
        )
    return out
