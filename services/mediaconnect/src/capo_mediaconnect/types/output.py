"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Output``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_integer
    import capo_mediaconnect.types.__list_of_media_stream_output_configuration
    import capo_mediaconnect.types.encryption
    import capo_mediaconnect.types.flow_transit_encryption
    import capo_mediaconnect.types.output_status
    import capo_mediaconnect.types.state
    import capo_mediaconnect.types.transport
    import capo_mediaconnect.types.vpc_interface_attachment


class Output(TypedDict, closed=True):
    data_transfer_subscriber_fee_percent: NotRequired["int"]
    """<p> Percentage from 0-100 of the data transfer cost to be billed to the subscriber.</p>"""
    description: NotRequired["str"]
    """<p> A description of the output.</p>"""
    destination: NotRequired["str"]
    """<p> The address where you want to send the output.</p>"""
    encryption: NotRequired["capo_mediaconnect.types.encryption.Encryption"]
    """<p> The type of key used for the encryption. If no keyType is provided, the service will use the default setting (static-key).</p>"""
    entitlement_arn: NotRequired["str"]
    """<p> The ARN of the entitlement on the originator''s flow. This value is relevant only on entitled flows.</p>"""
    listener_address: NotRequired["str"]
    """<p> The IP address that the receiver requires in order to establish a connection with the flow. For public networking, the ListenerAddress is represented by the elastic IP address of the flow. For private networking, the ListenerAddress is represented by the elastic network interface IP address of the VPC. This field applies only to outputs that use the Zixi pull or SRT listener protocol.</p>"""
    media_live_input_arn: NotRequired["str"]
    """<p> The input ARN of the MediaLive channel. This parameter is relevant only for outputs that were added by creating a MediaLive input.</p>"""
    media_stream_output_configurations: NotRequired[
        "capo_mediaconnect.types.__list_of_media_stream_output_configuration.__listOfMediaStreamOutputConfiguration"
    ]
    """<p> The configuration for each media stream that is associated with the output.</p>"""
    name: NotRequired["str"]
    """<p> The name of the output. This value must be unique within the current flow.</p>"""
    output_arn: NotRequired["str"]
    """<p> The ARN of the output.</p>"""
    port: NotRequired["int"]
    """<p> The port to use when content is distributed to this output.</p>"""
    transport: NotRequired["capo_mediaconnect.types.transport.Transport"]
    """<p> Attributes related to the transport stream that are used in the output.</p>"""
    vpc_interface_attachment: NotRequired[
        "capo_mediaconnect.types.vpc_interface_attachment.VpcInterfaceAttachment"
    ]
    """<p> The name of the VPC interface attachment to use for this output.</p>"""
    bridge_arn: NotRequired["str"]
    """<p> The ARN of the bridge added to this output.</p>"""
    bridge_ports: NotRequired[
        "capo_mediaconnect.types.__list_of_integer.__listOfInteger"
    ]
    """<p> The bridge output ports currently in use.</p>"""
    output_status: NotRequired["capo_mediaconnect.types.output_status.OutputStatus"]
    """<p> An indication of whether the output is transmitting data or not.</p>"""
    peer_ip_address: NotRequired["str"]
    """<p>The IP address of the device that is currently receiving content from this output.</p> <note> <ul> <li> <p>For outputs that use protocols where you specify the destination (such as SRT Caller or Zixi Push), this value matches the configured destination address.</p> </li> <li> <p>For outputs that use listener protocols (such as SRT Listener), this value shows the address of the connected receiver. </p> </li> <li> <p>Peer IP addresses aren't available for entitlements, managed MediaLive outputs, NDI® sources and outputs, and CDI/ST2110 outputs. </p> </li> <li> <p>The peer IP address might not be visible for flows that haven't been started yet, or flows that were started before May 2025. In these cases, restart your flow to see the peer IP address.</p> </li> </ul> </note>"""
    router_integration_state: NotRequired["capo_mediaconnect.types.state.State"]
    """<p>Indicates if router integration is enabled or disabled on the flow output.</p>"""
    router_integration_transit_encryption: NotRequired[
        "capo_mediaconnect.types.flow_transit_encryption.FlowTransitEncryption"
    ]
    """<p>The encryption configuration for the output when router integration is enabled.</p>"""
    connected_router_input_arn: NotRequired["str"]
    """<p>The ARN of the router input that's connected to this flow output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Output) -> dict:
    out: dict = {}
    if "data_transfer_subscriber_fee_percent" in value:
        out["dataTransferSubscriberFeePercent"] = value[
            "data_transfer_subscriber_fee_percent"
        ]
    if "description" in value:
        out["description"] = value["description"]
    if "destination" in value:
        out["destination"] = value["destination"]
    if "encryption" in value:
        import capo_mediaconnect.types.encryption

        out["encryption"] = capo_mediaconnect.types.encryption.serialize_json(
            value["encryption"]
        )
    if "entitlement_arn" in value:
        out["entitlementArn"] = value["entitlement_arn"]
    if "listener_address" in value:
        out["listenerAddress"] = value["listener_address"]
    if "media_live_input_arn" in value:
        out["mediaLiveInputArn"] = value["media_live_input_arn"]
    if "media_stream_output_configurations" in value:
        import capo_mediaconnect.types.__list_of_media_stream_output_configuration

        out["mediaStreamOutputConfigurations"] = (
            capo_mediaconnect.types.__list_of_media_stream_output_configuration.serialize_json(
                value["media_stream_output_configurations"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "output_arn" in value:
        out["outputArn"] = value["output_arn"]
    if "port" in value:
        out["port"] = value["port"]
    if "transport" in value:
        import capo_mediaconnect.types.transport

        out["transport"] = capo_mediaconnect.types.transport.serialize_json(
            value["transport"]
        )
    if "vpc_interface_attachment" in value:
        import capo_mediaconnect.types.vpc_interface_attachment

        out["vpcInterfaceAttachment"] = (
            capo_mediaconnect.types.vpc_interface_attachment.serialize_json(
                value["vpc_interface_attachment"]
            )
        )
    if "bridge_arn" in value:
        out["bridgeArn"] = value["bridge_arn"]
    if "bridge_ports" in value:
        import capo_mediaconnect.types.__list_of_integer

        out["bridgePorts"] = capo_mediaconnect.types.__list_of_integer.serialize_json(
            value["bridge_ports"]
        )
    if "output_status" in value:
        import capo_mediaconnect.types.output_status

        out["outputStatus"] = capo_mediaconnect.types.output_status.serialize_json(
            value["output_status"]
        )
    if "peer_ip_address" in value:
        out["peerIpAddress"] = value["peer_ip_address"]
    if "router_integration_state" in value:
        import capo_mediaconnect.types.state

        out["routerIntegrationState"] = capo_mediaconnect.types.state.serialize_json(
            value["router_integration_state"]
        )
    if "router_integration_transit_encryption" in value:
        import capo_mediaconnect.types.flow_transit_encryption

        out["routerIntegrationTransitEncryption"] = (
            capo_mediaconnect.types.flow_transit_encryption.serialize_json(
                value["router_integration_transit_encryption"]
            )
        )
    if "connected_router_input_arn" in value:
        out["connectedRouterInputArn"] = value["connected_router_input_arn"]
    return out


def deserialize_json(data: dict) -> Output:
    out: Output = {}  # type: ignore[typeddict-item]
    if "dataTransferSubscriberFeePercent" in data:
        out["data_transfer_subscriber_fee_percent"] = data[
            "dataTransferSubscriberFeePercent"
        ]
    if "description" in data:
        out["description"] = data["description"]
    if "destination" in data:
        out["destination"] = data["destination"]
    if "encryption" in data:
        import capo_mediaconnect.types.encryption

        out["encryption"] = capo_mediaconnect.types.encryption.deserialize_json(
            data["encryption"]
        )
    if "entitlementArn" in data:
        out["entitlement_arn"] = data["entitlementArn"]
    if "listenerAddress" in data:
        out["listener_address"] = data["listenerAddress"]
    if "mediaLiveInputArn" in data:
        out["media_live_input_arn"] = data["mediaLiveInputArn"]
    if "mediaStreamOutputConfigurations" in data:
        import capo_mediaconnect.types.__list_of_media_stream_output_configuration

        out["media_stream_output_configurations"] = (
            capo_mediaconnect.types.__list_of_media_stream_output_configuration.deserialize_json(
                data["mediaStreamOutputConfigurations"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "outputArn" in data:
        out["output_arn"] = data["outputArn"]
    if "port" in data:
        out["port"] = data["port"]
    if "transport" in data:
        import capo_mediaconnect.types.transport

        out["transport"] = capo_mediaconnect.types.transport.deserialize_json(
            data["transport"]
        )
    if "vpcInterfaceAttachment" in data:
        import capo_mediaconnect.types.vpc_interface_attachment

        out["vpc_interface_attachment"] = (
            capo_mediaconnect.types.vpc_interface_attachment.deserialize_json(
                data["vpcInterfaceAttachment"]
            )
        )
    if "bridgeArn" in data:
        out["bridge_arn"] = data["bridgeArn"]
    if "bridgePorts" in data:
        import capo_mediaconnect.types.__list_of_integer

        out["bridge_ports"] = (
            capo_mediaconnect.types.__list_of_integer.deserialize_json(
                data["bridgePorts"]
            )
        )
    if "outputStatus" in data:
        import capo_mediaconnect.types.output_status

        out["output_status"] = capo_mediaconnect.types.output_status.deserialize_json(
            data["outputStatus"]
        )
    if "peerIpAddress" in data:
        out["peer_ip_address"] = data["peerIpAddress"]
    if "routerIntegrationState" in data:
        import capo_mediaconnect.types.state

        out["router_integration_state"] = (
            capo_mediaconnect.types.state.deserialize_json(
                data["routerIntegrationState"]
            )
        )
    if "routerIntegrationTransitEncryption" in data:
        import capo_mediaconnect.types.flow_transit_encryption

        out["router_integration_transit_encryption"] = (
            capo_mediaconnect.types.flow_transit_encryption.deserialize_json(
                data["routerIntegrationTransitEncryption"]
            )
        )
    if "connectedRouterInputArn" in data:
        out["connected_router_input_arn"] = data["connectedRouterInputArn"]
    return out
