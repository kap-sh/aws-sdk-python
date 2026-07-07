"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateChannelRequest``."""

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
    import aws_sdk_medialive.types.channel_engine_version_request
    import aws_sdk_medialive.types.encoder_settings
    import aws_sdk_medialive.types.inference_settings
    import aws_sdk_medialive.types.input_specification
    import aws_sdk_medialive.types.linked_channel_settings
    import aws_sdk_medialive.types.log_level
    import aws_sdk_medialive.types.maintenance_update_settings
    import aws_sdk_medialive.types.special_router_settings


class UpdateChannelRequest(TypedDict, closed=True):
    cdi_input_specification: NotRequired[
        "aws_sdk_medialive.types.cdi_input_specification.CdiInputSpecification"
    ]
    """Specification of CDI inputs for this channel"""
    channel_id: "aws_sdk_medialive.types.__string.__string"
    """channel ID"""
    destinations: NotRequired[
        "aws_sdk_medialive.types.__list_of_output_destination.__listOfOutputDestination"
    ]
    """A list of output destinations for this channel."""
    encoder_settings: NotRequired[
        "aws_sdk_medialive.types.encoder_settings.EncoderSettings"
    ]
    """The encoder settings for this channel."""
    input_attachments: NotRequired[
        "aws_sdk_medialive.types.__list_of_input_attachment.__listOfInputAttachment"
    ]
    input_specification: NotRequired[
        "aws_sdk_medialive.types.input_specification.InputSpecification"
    ]
    """Specification of network and file inputs for this channel"""
    log_level: NotRequired["aws_sdk_medialive.types.log_level.LogLevel"]
    """The log level to write to CloudWatch Logs."""
    maintenance: NotRequired[
        "aws_sdk_medialive.types.maintenance_update_settings.MaintenanceUpdateSettings"
    ]
    """Maintenance settings for this channel."""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The name of the channel."""
    role_arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """An optional Amazon Resource Name (ARN) of the role to assume when running the Channel. If you do not specify this on an update call but the role was previously set that role will be removed."""
    channel_engine_version: NotRequired[
        "aws_sdk_medialive.types.channel_engine_version_request.ChannelEngineVersionRequest"
    ]
    """Channel engine version for this channel"""
    dry_run: NotRequired["aws_sdk_medialive.types.__boolean.__boolean"]
    anywhere_settings: NotRequired[
        "aws_sdk_medialive.types.anywhere_settings.AnywhereSettings"
    ]
    """The Elemental Anywhere settings for this channel."""
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
    special_router_settings: NotRequired[
        "aws_sdk_medialive.types.special_router_settings.SpecialRouterSettings"
    ]
    """When using MediaConnect Router as the source of a MediaLive input there's a special handoff that occurs when a router output is created. This group of settings is set on your behalf by the MediaConnect Router service using this set of settings. This setting object can only by used by that service."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelRequest) -> dict:
    out: dict = {}
    if "cdi_input_specification" in value:
        import aws_sdk_medialive.types.cdi_input_specification

        out["cdiInputSpecification"] = (
            aws_sdk_medialive.types.cdi_input_specification.serialize_json(
                value["cdi_input_specification"]
            )
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
        import aws_sdk_medialive.types.maintenance_update_settings

        out["maintenance"] = (
            aws_sdk_medialive.types.maintenance_update_settings.serialize_json(
                value["maintenance"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "channel_engine_version" in value:
        import aws_sdk_medialive.types.channel_engine_version_request

        out["channelEngineVersion"] = (
            aws_sdk_medialive.types.channel_engine_version_request.serialize_json(
                value["channel_engine_version"]
            )
        )
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    if "anywhere_settings" in value:
        import aws_sdk_medialive.types.anywhere_settings

        out["anywhereSettings"] = (
            aws_sdk_medialive.types.anywhere_settings.serialize_json(
                value["anywhere_settings"]
            )
        )
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
    if "special_router_settings" in value:
        import aws_sdk_medialive.types.special_router_settings

        out["specialRouterSettings"] = (
            aws_sdk_medialive.types.special_router_settings.serialize_json(
                value["special_router_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateChannelRequest:
    out: UpdateChannelRequest = {}  # type: ignore[typeddict-item]
    if "cdiInputSpecification" in data:
        import aws_sdk_medialive.types.cdi_input_specification

        out["cdi_input_specification"] = (
            aws_sdk_medialive.types.cdi_input_specification.deserialize_json(
                data["cdiInputSpecification"]
            )
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
        import aws_sdk_medialive.types.maintenance_update_settings

        out["maintenance"] = (
            aws_sdk_medialive.types.maintenance_update_settings.deserialize_json(
                data["maintenance"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "channelEngineVersion" in data:
        import aws_sdk_medialive.types.channel_engine_version_request

        out["channel_engine_version"] = (
            aws_sdk_medialive.types.channel_engine_version_request.deserialize_json(
                data["channelEngineVersion"]
            )
        )
    if "dryRun" in data:
        out["dry_run"] = data["dryRun"]
    if "anywhereSettings" in data:
        import aws_sdk_medialive.types.anywhere_settings

        out["anywhere_settings"] = (
            aws_sdk_medialive.types.anywhere_settings.deserialize_json(
                data["anywhereSettings"]
            )
        )
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
    if "specialRouterSettings" in data:
        import aws_sdk_medialive.types.special_router_settings

        out["special_router_settings"] = (
            aws_sdk_medialive.types.special_router_settings.deserialize_json(
                data["specialRouterSettings"]
            )
        )
    return out
