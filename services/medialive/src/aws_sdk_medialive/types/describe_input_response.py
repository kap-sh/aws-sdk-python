"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeInputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of__string
    import aws_sdk_medialive.types.__list_of_input_destination
    import aws_sdk_medialive.types.__list_of_input_device_settings
    import aws_sdk_medialive.types.__list_of_input_source
    import aws_sdk_medialive.types.__list_of_media_connect_flow
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.input_class
    import aws_sdk_medialive.types.input_network_location
    import aws_sdk_medialive.types.input_sdi_sources
    import aws_sdk_medialive.types.input_source_type
    import aws_sdk_medialive.types.input_state
    import aws_sdk_medialive.types.input_type
    import aws_sdk_medialive.types.multicast_settings
    import aws_sdk_medialive.types.router_input_settings
    import aws_sdk_medialive.types.smpte2110_receiver_group_settings
    import aws_sdk_medialive.types.srt_settings
    import aws_sdk_medialive.types.tags


class DescribeInputResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The Unique ARN of the input (generated, immutable)."""
    attached_channels: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """A list of channel IDs that that input is attached to (currently an input can only be attached to one channel)."""
    destinations: NotRequired[
        "aws_sdk_medialive.types.__list_of_input_destination.__listOfInputDestination"
    ]
    """A list of the destinations of the input (PUSH-type)."""
    id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The generated ID of the input (unique for user account, immutable)."""
    input_class: NotRequired["aws_sdk_medialive.types.input_class.InputClass"]
    """STANDARD - MediaLive expects two sources to be connected to this input. If the channel is also STANDARD, both sources will be ingested. If the channel is SINGLE_PIPELINE, only the first source will be ingested; the second source will always be ignored, even if the first source fails. SINGLE_PIPELINE - You can connect only one source to this input. If the ChannelClass is also SINGLE_PIPELINE, this value is valid. If the ChannelClass is STANDARD, this value is not valid because the channel requires two sources in the input."""
    input_devices: NotRequired[
        "aws_sdk_medialive.types.__list_of_input_device_settings.__listOfInputDeviceSettings"
    ]
    """Settings for the input devices."""
    input_partner_ids: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """A list of IDs for all Inputs which are partners of this one."""
    input_source_type: NotRequired[
        "aws_sdk_medialive.types.input_source_type.InputSourceType"
    ]
    """Certain pull input sources can be dynamic, meaning that they can have their URL's dynamically changes during input switch actions. Presently, this functionality only works with MP4_FILE and TS_FILE inputs."""
    media_connect_flows: NotRequired[
        "aws_sdk_medialive.types.__list_of_media_connect_flow.__listOfMediaConnectFlow"
    ]
    """A list of MediaConnect Flows for this input."""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The user-assigned name (This is a mutable value)."""
    role_arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The Amazon Resource Name (ARN) of the role this input assumes during and after creation."""
    security_groups: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """A list of IDs for all the Input Security Groups attached to the input."""
    sources: NotRequired[
        "aws_sdk_medialive.types.__list_of_input_source.__listOfInputSource"
    ]
    """A list of the sources of the input (PULL-type)."""
    state: NotRequired["aws_sdk_medialive.types.input_state.InputState"]
    tags: NotRequired["aws_sdk_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""
    type: NotRequired["aws_sdk_medialive.types.input_type.InputType"]
    srt_settings: NotRequired["aws_sdk_medialive.types.srt_settings.SrtSettings"]
    """The settings associated with an SRT input."""
    input_network_location: NotRequired[
        "aws_sdk_medialive.types.input_network_location.InputNetworkLocation"
    ]
    """The location of this input. AWS, for an input existing in the AWS Cloud, On-Prem for an input in a customer network."""
    multicast_settings: NotRequired[
        "aws_sdk_medialive.types.multicast_settings.MulticastSettings"
    ]
    """Multicast Input settings."""
    smpte2110_receiver_group_settings: NotRequired[
        "aws_sdk_medialive.types.smpte2110_receiver_group_settings.Smpte2110ReceiverGroupSettings"
    ]
    """Include this parameter if the input is a SMPTE 2110 input, to identify the stream sources for this input."""
    sdi_sources: NotRequired[
        "aws_sdk_medialive.types.input_sdi_sources.InputSdiSources"
    ]
    router_settings: NotRequired[
        "aws_sdk_medialive.types.router_input_settings.RouterInputSettings"
    ]
    """Information about any MediaConnect router association with this input."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInputResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "attached_channels" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["attachedChannels"] = (
            aws_sdk_medialive.types.__list_of__string.serialize_json(
                value["attached_channels"]
            )
        )
    if "destinations" in value:
        import aws_sdk_medialive.types.__list_of_input_destination

        out["destinations"] = (
            aws_sdk_medialive.types.__list_of_input_destination.serialize_json(
                value["destinations"]
            )
        )
    if "id" in value:
        out["id"] = value["id"]
    if "input_class" in value:
        import aws_sdk_medialive.types.input_class

        out["inputClass"] = aws_sdk_medialive.types.input_class.serialize_json(
            value["input_class"]
        )
    if "input_devices" in value:
        import aws_sdk_medialive.types.__list_of_input_device_settings

        out["inputDevices"] = (
            aws_sdk_medialive.types.__list_of_input_device_settings.serialize_json(
                value["input_devices"]
            )
        )
    if "input_partner_ids" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["inputPartnerIds"] = (
            aws_sdk_medialive.types.__list_of__string.serialize_json(
                value["input_partner_ids"]
            )
        )
    if "input_source_type" in value:
        import aws_sdk_medialive.types.input_source_type

        out["inputSourceType"] = (
            aws_sdk_medialive.types.input_source_type.serialize_json(
                value["input_source_type"]
            )
        )
    if "media_connect_flows" in value:
        import aws_sdk_medialive.types.__list_of_media_connect_flow

        out["mediaConnectFlows"] = (
            aws_sdk_medialive.types.__list_of_media_connect_flow.serialize_json(
                value["media_connect_flows"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "security_groups" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["securityGroups"] = (
            aws_sdk_medialive.types.__list_of__string.serialize_json(
                value["security_groups"]
            )
        )
    if "sources" in value:
        import aws_sdk_medialive.types.__list_of_input_source

        out["sources"] = aws_sdk_medialive.types.__list_of_input_source.serialize_json(
            value["sources"]
        )
    if "state" in value:
        import aws_sdk_medialive.types.input_state

        out["state"] = aws_sdk_medialive.types.input_state.serialize_json(
            value["state"]
        )
    if "tags" in value:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.serialize_json(value["tags"])
    if "type" in value:
        import aws_sdk_medialive.types.input_type

        out["type"] = aws_sdk_medialive.types.input_type.serialize_json(value["type"])
    if "srt_settings" in value:
        import aws_sdk_medialive.types.srt_settings

        out["srtSettings"] = aws_sdk_medialive.types.srt_settings.serialize_json(
            value["srt_settings"]
        )
    if "input_network_location" in value:
        import aws_sdk_medialive.types.input_network_location

        out["inputNetworkLocation"] = (
            aws_sdk_medialive.types.input_network_location.serialize_json(
                value["input_network_location"]
            )
        )
    if "multicast_settings" in value:
        import aws_sdk_medialive.types.multicast_settings

        out["multicastSettings"] = (
            aws_sdk_medialive.types.multicast_settings.serialize_json(
                value["multicast_settings"]
            )
        )
    if "smpte2110_receiver_group_settings" in value:
        import aws_sdk_medialive.types.smpte2110_receiver_group_settings

        out["smpte2110ReceiverGroupSettings"] = (
            aws_sdk_medialive.types.smpte2110_receiver_group_settings.serialize_json(
                value["smpte2110_receiver_group_settings"]
            )
        )
    if "sdi_sources" in value:
        import aws_sdk_medialive.types.input_sdi_sources

        out["sdiSources"] = aws_sdk_medialive.types.input_sdi_sources.serialize_json(
            value["sdi_sources"]
        )
    if "router_settings" in value:
        import aws_sdk_medialive.types.router_input_settings

        out["routerSettings"] = (
            aws_sdk_medialive.types.router_input_settings.serialize_json(
                value["router_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeInputResponse:
    out: DescribeInputResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "attachedChannels" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["attached_channels"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["attachedChannels"]
            )
        )
    if "destinations" in data:
        import aws_sdk_medialive.types.__list_of_input_destination

        out["destinations"] = (
            aws_sdk_medialive.types.__list_of_input_destination.deserialize_json(
                data["destinations"]
            )
        )
    if "id" in data:
        out["id"] = data["id"]
    if "inputClass" in data:
        import aws_sdk_medialive.types.input_class

        out["input_class"] = aws_sdk_medialive.types.input_class.deserialize_json(
            data["inputClass"]
        )
    if "inputDevices" in data:
        import aws_sdk_medialive.types.__list_of_input_device_settings

        out["input_devices"] = (
            aws_sdk_medialive.types.__list_of_input_device_settings.deserialize_json(
                data["inputDevices"]
            )
        )
    if "inputPartnerIds" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["input_partner_ids"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["inputPartnerIds"]
            )
        )
    if "inputSourceType" in data:
        import aws_sdk_medialive.types.input_source_type

        out["input_source_type"] = (
            aws_sdk_medialive.types.input_source_type.deserialize_json(
                data["inputSourceType"]
            )
        )
    if "mediaConnectFlows" in data:
        import aws_sdk_medialive.types.__list_of_media_connect_flow

        out["media_connect_flows"] = (
            aws_sdk_medialive.types.__list_of_media_connect_flow.deserialize_json(
                data["mediaConnectFlows"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "securityGroups" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["security_groups"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["securityGroups"]
            )
        )
    if "sources" in data:
        import aws_sdk_medialive.types.__list_of_input_source

        out["sources"] = (
            aws_sdk_medialive.types.__list_of_input_source.deserialize_json(
                data["sources"]
            )
        )
    if "state" in data:
        import aws_sdk_medialive.types.input_state

        out["state"] = aws_sdk_medialive.types.input_state.deserialize_json(
            data["state"]
        )
    if "tags" in data:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.deserialize_json(data["tags"])
    if "type" in data:
        import aws_sdk_medialive.types.input_type

        out["type"] = aws_sdk_medialive.types.input_type.deserialize_json(data["type"])
    if "srtSettings" in data:
        import aws_sdk_medialive.types.srt_settings

        out["srt_settings"] = aws_sdk_medialive.types.srt_settings.deserialize_json(
            data["srtSettings"]
        )
    if "inputNetworkLocation" in data:
        import aws_sdk_medialive.types.input_network_location

        out["input_network_location"] = (
            aws_sdk_medialive.types.input_network_location.deserialize_json(
                data["inputNetworkLocation"]
            )
        )
    if "multicastSettings" in data:
        import aws_sdk_medialive.types.multicast_settings

        out["multicast_settings"] = (
            aws_sdk_medialive.types.multicast_settings.deserialize_json(
                data["multicastSettings"]
            )
        )
    if "smpte2110ReceiverGroupSettings" in data:
        import aws_sdk_medialive.types.smpte2110_receiver_group_settings

        out["smpte2110_receiver_group_settings"] = (
            aws_sdk_medialive.types.smpte2110_receiver_group_settings.deserialize_json(
                data["smpte2110ReceiverGroupSettings"]
            )
        )
    if "sdiSources" in data:
        import aws_sdk_medialive.types.input_sdi_sources

        out["sdi_sources"] = aws_sdk_medialive.types.input_sdi_sources.deserialize_json(
            data["sdiSources"]
        )
    if "routerSettings" in data:
        import aws_sdk_medialive.types.router_input_settings

        out["router_settings"] = (
            aws_sdk_medialive.types.router_input_settings.deserialize_json(
                data["routerSettings"]
            )
        )
    return out
