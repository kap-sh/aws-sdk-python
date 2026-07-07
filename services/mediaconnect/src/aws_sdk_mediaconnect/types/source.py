"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Source``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_media_stream_source_configuration
    import aws_sdk_mediaconnect.types.encryption
    import aws_sdk_mediaconnect.types.flow_transit_encryption
    import aws_sdk_mediaconnect.types.gateway_bridge_source
    import aws_sdk_mediaconnect.types.state
    import aws_sdk_mediaconnect.types.transport


class Source(TypedDict, closed=True):
    data_transfer_subscriber_fee_percent: NotRequired["int"]
    """<p> Percentage from 0-100 of the data transfer cost to be billed to the subscriber.</p>"""
    decryption: NotRequired["aws_sdk_mediaconnect.types.encryption.Encryption"]
    """<p> The type of encryption that is used on the content ingested from this source.</p>"""
    description: NotRequired["str"]
    """<p> A description for the source. This value is not used or seen outside of the current MediaConnect account.</p>"""
    entitlement_arn: NotRequired["str"]
    """<p> The ARN of the entitlement that allows you to subscribe to content that comes from another Amazon Web Services account. The entitlement is set by the content originator and the ARN is generated as part of the originator's flow.</p>"""
    ingest_ip: NotRequired["str"]
    """<p> The IP address that the flow will be listening on for incoming content.</p>"""
    ingest_port: NotRequired["int"]
    """<p> The port that the flow will be listening on for incoming content.</p>"""
    media_stream_source_configurations: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_media_stream_source_configuration.__listOfMediaStreamSourceConfiguration"
    ]
    """<p> The media streams that are associated with the source, and the parameters for those associations.</p>"""
    name: NotRequired["str"]
    """<p> The name of the source.</p>"""
    sender_control_port: NotRequired["int"]
    """<p> The IP address that the flow communicates with to initiate connection with the sender.</p>"""
    sender_ip_address: NotRequired["str"]
    """<p> The port that the flow uses to send outbound requests to initiate connection with the sender.</p>"""
    source_arn: NotRequired["str"]
    """<p> The ARN of the source.</p>"""
    transport: NotRequired["aws_sdk_mediaconnect.types.transport.Transport"]
    """<p> Attributes related to the transport stream that are used in the source.</p>"""
    vpc_interface_name: NotRequired["str"]
    """<p> The name of the VPC interface that is used for this source.</p>"""
    whitelist_cidr: NotRequired["str"]
    """<p> The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.</p>"""
    gateway_bridge_source: NotRequired[
        "aws_sdk_mediaconnect.types.gateway_bridge_source.GatewayBridgeSource"
    ]
    """<p> The source configuration for cloud flows receiving a stream from a bridge.</p>"""
    peer_ip_address: NotRequired["str"]
    """<p>The IP address of the device that is currently sending content to this source. </p> <note> <ul> <li> <p>For sources that use protocols where you specify the origin (such as SRT Caller), this value matches the configured origin address. </p> </li> <li> <p>For sources that use listener protocols (such as SRT Listener or RTP), this value shows the address of the connected sender. </p> </li> <li> <p>Peer IP addresses aren't available for entitlements and CDI/ST2110 sources.</p> </li> <li> <p>The peer IP address might not be visible for flows that haven't been started yet, or flows that were started before May 2025. In these cases, restart your flow to see the peer IP address.</p> </li> </ul> </note>"""
    router_integration_state: NotRequired["aws_sdk_mediaconnect.types.state.State"]
    """<p>Indicates if router integration is enabled or disabled on the flow source.</p>"""
    router_integration_transit_decryption: NotRequired[
        "aws_sdk_mediaconnect.types.flow_transit_encryption.FlowTransitEncryption"
    ]
    """<p>The decryption configuration for the flow source when router integration is enabled.</p>"""
    connected_router_output_arn: NotRequired["str"]
    """<p>The ARN of the router output that's currently connected to this source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Source) -> dict:
    out: dict = {}
    if "data_transfer_subscriber_fee_percent" in value:
        out["dataTransferSubscriberFeePercent"] = value[
            "data_transfer_subscriber_fee_percent"
        ]
    if "decryption" in value:
        import aws_sdk_mediaconnect.types.encryption

        out["decryption"] = aws_sdk_mediaconnect.types.encryption.serialize_json(
            value["decryption"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "entitlement_arn" in value:
        out["entitlementArn"] = value["entitlement_arn"]
    if "ingest_ip" in value:
        out["ingestIp"] = value["ingest_ip"]
    if "ingest_port" in value:
        out["ingestPort"] = value["ingest_port"]
    if "media_stream_source_configurations" in value:
        import aws_sdk_mediaconnect.types.__list_of_media_stream_source_configuration

        out["mediaStreamSourceConfigurations"] = (
            aws_sdk_mediaconnect.types.__list_of_media_stream_source_configuration.serialize_json(
                value["media_stream_source_configurations"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "sender_control_port" in value:
        out["senderControlPort"] = value["sender_control_port"]
    if "sender_ip_address" in value:
        out["senderIpAddress"] = value["sender_ip_address"]
    if "source_arn" in value:
        out["sourceArn"] = value["source_arn"]
    if "transport" in value:
        import aws_sdk_mediaconnect.types.transport

        out["transport"] = aws_sdk_mediaconnect.types.transport.serialize_json(
            value["transport"]
        )
    if "vpc_interface_name" in value:
        out["vpcInterfaceName"] = value["vpc_interface_name"]
    if "whitelist_cidr" in value:
        out["whitelistCidr"] = value["whitelist_cidr"]
    if "gateway_bridge_source" in value:
        import aws_sdk_mediaconnect.types.gateway_bridge_source

        out["gatewayBridgeSource"] = (
            aws_sdk_mediaconnect.types.gateway_bridge_source.serialize_json(
                value["gateway_bridge_source"]
            )
        )
    if "peer_ip_address" in value:
        out["peerIpAddress"] = value["peer_ip_address"]
    if "router_integration_state" in value:
        import aws_sdk_mediaconnect.types.state

        out["routerIntegrationState"] = aws_sdk_mediaconnect.types.state.serialize_json(
            value["router_integration_state"]
        )
    if "router_integration_transit_decryption" in value:
        import aws_sdk_mediaconnect.types.flow_transit_encryption

        out["routerIntegrationTransitDecryption"] = (
            aws_sdk_mediaconnect.types.flow_transit_encryption.serialize_json(
                value["router_integration_transit_decryption"]
            )
        )
    if "connected_router_output_arn" in value:
        out["connectedRouterOutputArn"] = value["connected_router_output_arn"]
    return out


def deserialize_json(data: dict) -> Source:
    out: Source = {}  # type: ignore[typeddict-item]
    if "dataTransferSubscriberFeePercent" in data:
        out["data_transfer_subscriber_fee_percent"] = data[
            "dataTransferSubscriberFeePercent"
        ]
    if "decryption" in data:
        import aws_sdk_mediaconnect.types.encryption

        out["decryption"] = aws_sdk_mediaconnect.types.encryption.deserialize_json(
            data["decryption"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "entitlementArn" in data:
        out["entitlement_arn"] = data["entitlementArn"]
    if "ingestIp" in data:
        out["ingest_ip"] = data["ingestIp"]
    if "ingestPort" in data:
        out["ingest_port"] = data["ingestPort"]
    if "mediaStreamSourceConfigurations" in data:
        import aws_sdk_mediaconnect.types.__list_of_media_stream_source_configuration

        out["media_stream_source_configurations"] = (
            aws_sdk_mediaconnect.types.__list_of_media_stream_source_configuration.deserialize_json(
                data["mediaStreamSourceConfigurations"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "senderControlPort" in data:
        out["sender_control_port"] = data["senderControlPort"]
    if "senderIpAddress" in data:
        out["sender_ip_address"] = data["senderIpAddress"]
    if "sourceArn" in data:
        out["source_arn"] = data["sourceArn"]
    if "transport" in data:
        import aws_sdk_mediaconnect.types.transport

        out["transport"] = aws_sdk_mediaconnect.types.transport.deserialize_json(
            data["transport"]
        )
    if "vpcInterfaceName" in data:
        out["vpc_interface_name"] = data["vpcInterfaceName"]
    if "whitelistCidr" in data:
        out["whitelist_cidr"] = data["whitelistCidr"]
    if "gatewayBridgeSource" in data:
        import aws_sdk_mediaconnect.types.gateway_bridge_source

        out["gateway_bridge_source"] = (
            aws_sdk_mediaconnect.types.gateway_bridge_source.deserialize_json(
                data["gatewayBridgeSource"]
            )
        )
    if "peerIpAddress" in data:
        out["peer_ip_address"] = data["peerIpAddress"]
    if "routerIntegrationState" in data:
        import aws_sdk_mediaconnect.types.state

        out["router_integration_state"] = (
            aws_sdk_mediaconnect.types.state.deserialize_json(
                data["routerIntegrationState"]
            )
        )
    if "routerIntegrationTransitDecryption" in data:
        import aws_sdk_mediaconnect.types.flow_transit_encryption

        out["router_integration_transit_decryption"] = (
            aws_sdk_mediaconnect.types.flow_transit_encryption.deserialize_json(
                data["routerIntegrationTransitDecryption"]
            )
        )
    if "connectedRouterOutputArn" in data:
        out["connected_router_output_arn"] = data["connectedRouterOutputArn"]
    return out
