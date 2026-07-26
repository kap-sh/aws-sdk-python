"""Generated from Smithy shape ``com.amazonaws.medialive#CreateInputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of__string
    import capo_medialive.types.__list_of_input_destination_request
    import capo_medialive.types.__list_of_input_device_settings
    import capo_medialive.types.__list_of_input_source_request
    import capo_medialive.types.__list_of_media_connect_flow_request
    import capo_medialive.types.__string
    import capo_medialive.types.input_network_location
    import capo_medialive.types.input_sdi_sources
    import capo_medialive.types.input_type
    import capo_medialive.types.input_vpc_request
    import capo_medialive.types.multicast_settings_create_request
    import capo_medialive.types.router_settings
    import capo_medialive.types.smpte2110_receiver_group_settings
    import capo_medialive.types.srt_settings_request
    import capo_medialive.types.tags


class CreateInputRequest(TypedDict, closed=True):
    destinations: NotRequired[
        "capo_medialive.types.__list_of_input_destination_request.__listOfInputDestinationRequest"
    ]
    """Destination settings for PUSH type inputs."""
    input_devices: NotRequired[
        "capo_medialive.types.__list_of_input_device_settings.__listOfInputDeviceSettings"
    ]
    """Settings for the devices."""
    input_security_groups: NotRequired[
        "capo_medialive.types.__list_of__string.__listOf__string"
    ]
    """A list of security groups referenced by IDs to attach to the input."""
    media_connect_flows: NotRequired[
        "capo_medialive.types.__list_of_media_connect_flow_request.__listOfMediaConnectFlowRequest"
    ]
    """A list of the MediaConnect Flows that you want to use in this input. You can specify as few as one Flow and presently, as many as two. The only requirement is when you have more than one is that each Flow is in a separate Availability Zone as this ensures your EML input is redundant to AZ issues."""
    name: NotRequired["capo_medialive.types.__string.__string"]
    """Name of the input."""
    request_id: NotRequired["capo_medialive.types.__string.__string"]
    """Unique identifier of the request to ensure the request is handled exactly once in case of retries."""
    role_arn: NotRequired["capo_medialive.types.__string.__string"]
    """The Amazon Resource Name (ARN) of the role this input assumes during and after creation."""
    sources: NotRequired[
        "capo_medialive.types.__list_of_input_source_request.__listOfInputSourceRequest"
    ]
    """The source URLs for a PULL-type input. Every PULL type input needs exactly two source URLs for redundancy. Only specify sources for PULL type Inputs. Leave Destinations empty."""
    tags: NotRequired["capo_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""
    type: NotRequired["capo_medialive.types.input_type.InputType"]
    vpc: NotRequired["capo_medialive.types.input_vpc_request.InputVpcRequest"]
    srt_settings: NotRequired[
        "capo_medialive.types.srt_settings_request.SrtSettingsRequest"
    ]
    """The settings associated with an SRT input."""
    input_network_location: NotRequired[
        "capo_medialive.types.input_network_location.InputNetworkLocation"
    ]
    """The location of this input. AWS, for an input existing in the AWS Cloud, On-Prem for an input in a customer network."""
    multicast_settings: NotRequired[
        "capo_medialive.types.multicast_settings_create_request.MulticastSettingsCreateRequest"
    ]
    """Multicast Input settings."""
    smpte2110_receiver_group_settings: NotRequired[
        "capo_medialive.types.smpte2110_receiver_group_settings.Smpte2110ReceiverGroupSettings"
    ]
    """Include this parameter if the input is a SMPTE 2110 input, to identify the stream sources for this input."""
    sdi_sources: NotRequired["capo_medialive.types.input_sdi_sources.InputSdiSources"]
    router_settings: NotRequired["capo_medialive.types.router_settings.RouterSettings"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateInputRequest) -> dict:
    out: dict = {}
    if "destinations" in value:
        import capo_medialive.types.__list_of_input_destination_request

        out["destinations"] = (
            capo_medialive.types.__list_of_input_destination_request.serialize_json(
                value["destinations"]
            )
        )
    if "input_devices" in value:
        import capo_medialive.types.__list_of_input_device_settings

        out["inputDevices"] = (
            capo_medialive.types.__list_of_input_device_settings.serialize_json(
                value["input_devices"]
            )
        )
    if "input_security_groups" in value:
        import capo_medialive.types.__list_of__string

        out["inputSecurityGroups"] = (
            capo_medialive.types.__list_of__string.serialize_json(
                value["input_security_groups"]
            )
        )
    if "media_connect_flows" in value:
        import capo_medialive.types.__list_of_media_connect_flow_request

        out["mediaConnectFlows"] = (
            capo_medialive.types.__list_of_media_connect_flow_request.serialize_json(
                value["media_connect_flows"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "sources" in value:
        import capo_medialive.types.__list_of_input_source_request

        out["sources"] = (
            capo_medialive.types.__list_of_input_source_request.serialize_json(
                value["sources"]
            )
        )
    if "tags" in value:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.serialize_json(value["tags"])
    if "type" in value:
        import capo_medialive.types.input_type

        out["type"] = capo_medialive.types.input_type.serialize_json(value["type"])
    if "vpc" in value:
        import capo_medialive.types.input_vpc_request

        out["vpc"] = capo_medialive.types.input_vpc_request.serialize_json(value["vpc"])
    if "srt_settings" in value:
        import capo_medialive.types.srt_settings_request

        out["srtSettings"] = capo_medialive.types.srt_settings_request.serialize_json(
            value["srt_settings"]
        )
    if "input_network_location" in value:
        import capo_medialive.types.input_network_location

        out["inputNetworkLocation"] = (
            capo_medialive.types.input_network_location.serialize_json(
                value["input_network_location"]
            )
        )
    if "multicast_settings" in value:
        import capo_medialive.types.multicast_settings_create_request

        out["multicastSettings"] = (
            capo_medialive.types.multicast_settings_create_request.serialize_json(
                value["multicast_settings"]
            )
        )
    if "smpte2110_receiver_group_settings" in value:
        import capo_medialive.types.smpte2110_receiver_group_settings

        out["smpte2110ReceiverGroupSettings"] = (
            capo_medialive.types.smpte2110_receiver_group_settings.serialize_json(
                value["smpte2110_receiver_group_settings"]
            )
        )
    if "sdi_sources" in value:
        import capo_medialive.types.input_sdi_sources

        out["sdiSources"] = capo_medialive.types.input_sdi_sources.serialize_json(
            value["sdi_sources"]
        )
    if "router_settings" in value:
        import capo_medialive.types.router_settings

        out["routerSettings"] = capo_medialive.types.router_settings.serialize_json(
            value["router_settings"]
        )
    return out


def deserialize_json(data: dict) -> CreateInputRequest:
    out: CreateInputRequest = {}  # type: ignore[typeddict-item]
    if "destinations" in data:
        import capo_medialive.types.__list_of_input_destination_request

        out["destinations"] = (
            capo_medialive.types.__list_of_input_destination_request.deserialize_json(
                data["destinations"]
            )
        )
    if "inputDevices" in data:
        import capo_medialive.types.__list_of_input_device_settings

        out["input_devices"] = (
            capo_medialive.types.__list_of_input_device_settings.deserialize_json(
                data["inputDevices"]
            )
        )
    if "inputSecurityGroups" in data:
        import capo_medialive.types.__list_of__string

        out["input_security_groups"] = (
            capo_medialive.types.__list_of__string.deserialize_json(
                data["inputSecurityGroups"]
            )
        )
    if "mediaConnectFlows" in data:
        import capo_medialive.types.__list_of_media_connect_flow_request

        out["media_connect_flows"] = (
            capo_medialive.types.__list_of_media_connect_flow_request.deserialize_json(
                data["mediaConnectFlows"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "sources" in data:
        import capo_medialive.types.__list_of_input_source_request

        out["sources"] = (
            capo_medialive.types.__list_of_input_source_request.deserialize_json(
                data["sources"]
            )
        )
    if "tags" in data:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.deserialize_json(data["tags"])
    if "type" in data:
        import capo_medialive.types.input_type

        out["type"] = capo_medialive.types.input_type.deserialize_json(data["type"])
    if "vpc" in data:
        import capo_medialive.types.input_vpc_request

        out["vpc"] = capo_medialive.types.input_vpc_request.deserialize_json(
            data["vpc"]
        )
    if "srtSettings" in data:
        import capo_medialive.types.srt_settings_request

        out["srt_settings"] = (
            capo_medialive.types.srt_settings_request.deserialize_json(
                data["srtSettings"]
            )
        )
    if "inputNetworkLocation" in data:
        import capo_medialive.types.input_network_location

        out["input_network_location"] = (
            capo_medialive.types.input_network_location.deserialize_json(
                data["inputNetworkLocation"]
            )
        )
    if "multicastSettings" in data:
        import capo_medialive.types.multicast_settings_create_request

        out["multicast_settings"] = (
            capo_medialive.types.multicast_settings_create_request.deserialize_json(
                data["multicastSettings"]
            )
        )
    if "smpte2110ReceiverGroupSettings" in data:
        import capo_medialive.types.smpte2110_receiver_group_settings

        out["smpte2110_receiver_group_settings"] = (
            capo_medialive.types.smpte2110_receiver_group_settings.deserialize_json(
                data["smpte2110ReceiverGroupSettings"]
            )
        )
    if "sdiSources" in data:
        import capo_medialive.types.input_sdi_sources

        out["sdi_sources"] = capo_medialive.types.input_sdi_sources.deserialize_json(
            data["sdiSources"]
        )
    if "routerSettings" in data:
        import capo_medialive.types.router_settings

        out["router_settings"] = capo_medialive.types.router_settings.deserialize_json(
            data["routerSettings"]
        )
    return out
