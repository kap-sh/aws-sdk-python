"""Generated from Smithy shape ``com.amazonaws.rtbfabric#GetResponderGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_rtbfabric.types.domain_name
    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.gateway_type
    import aws_sdk_rtbfabric.types.listener_config
    import aws_sdk_rtbfabric.types.managed_endpoint_configuration
    import aws_sdk_rtbfabric.types.protocol
    import aws_sdk_rtbfabric.types.responder_gateway_status
    import aws_sdk_rtbfabric.types.security_group_id_list
    import aws_sdk_rtbfabric.types.subnet_id_list
    import aws_sdk_rtbfabric.types.tags_map
    import aws_sdk_rtbfabric.types.trust_store_configuration
    import aws_sdk_rtbfabric.types.vpc_id


class GetResponderGatewayResponse(TypedDict, closed=True):
    vpc_id: "aws_sdk_rtbfabric.types.vpc_id.VpcId"
    """<p>The unique identifier of the Virtual Private Cloud (VPC).</p>"""
    subnet_ids: "aws_sdk_rtbfabric.types.subnet_id_list.SubnetIdList"
    """<p>The unique identifiers of the subnets.</p>"""
    security_group_ids: (
        "aws_sdk_rtbfabric.types.security_group_id_list.SecurityGroupIdList"
    )
    """<p>The unique identifiers of the security groups.</p>"""
    status: "aws_sdk_rtbfabric.types.responder_gateway_status.ResponderGatewayStatus"
    """<p>The status of the request.</p>"""
    description: NotRequired["str"]
    """<p>The description of the responder gateway.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the responder gateway was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the responder gateway was updated.</p>"""
    domain_name: NotRequired["aws_sdk_rtbfabric.types.domain_name.DomainName"]
    """<p>The domain name of the responder gateway.</p>"""
    port: "int"
    """<p>The networking port.</p>"""
    protocol: "aws_sdk_rtbfabric.types.protocol.Protocol"
    """<p>The networking protocol.</p>"""
    listener_config: NotRequired[
        "aws_sdk_rtbfabric.types.listener_config.ListenerConfig"
    ]
    """<p>The listener configuration for the responder gateway.</p>"""
    trust_store_configuration: NotRequired[
        "aws_sdk_rtbfabric.types.trust_store_configuration.TrustStoreConfiguration"
    ]
    """<p>The configuration of the trust store.</p>"""
    managed_endpoint_configuration: NotRequired[
        "aws_sdk_rtbfabric.types.managed_endpoint_configuration.ManagedEndpointConfiguration"
    ]
    """<p>The configuration of the managed endpoint.</p>"""
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    tags: NotRequired["aws_sdk_rtbfabric.types.tags_map.TagsMap"]
    """<p>A map of the key-value pairs for the tag or tags assigned to the specified resource.</p>"""
    active_links_count: NotRequired["int"]
    """<p>The count of active links for the responder gateway.</p>"""
    total_links_count: NotRequired["int"]
    """<p>The total count of links for the responder gateway.</p>"""
    inbound_links_count: NotRequired["int"]
    """<p>Deprecated. Use 'linksRequestedCount' instead.</p>"""
    links_requested_count: NotRequired["int"]
    """<p>The count of requested links waiting for the responder gateway to accept or reject.</p>"""
    gateway_type: NotRequired["aws_sdk_rtbfabric.types.gateway_type.GatewayType"]
    """<p>The type of gateway. Valid values are <code>EXTERNAL</code> or <code>INTERNAL</code>.</p>"""
    external_inbound_endpoint: NotRequired[
        "aws_sdk_rtbfabric.types.domain_name.DomainName"
    ]
    """<p>The external inbound endpoint for the responder gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResponderGatewayResponse) -> dict:
    out: dict = {}
    out["vpcId"] = value["vpc_id"]
    import aws_sdk_rtbfabric.types.subnet_id_list

    out["subnetIds"] = aws_sdk_rtbfabric.types.subnet_id_list.serialize_json(
        value["subnet_ids"]
    )
    import aws_sdk_rtbfabric.types.security_group_id_list

    out["securityGroupIds"] = (
        aws_sdk_rtbfabric.types.security_group_id_list.serialize_json(
            value["security_group_ids"]
        )
    )
    import aws_sdk_rtbfabric.types.responder_gateway_status

    out["status"] = aws_sdk_rtbfabric.types.responder_gateway_status.serialize_json(
        value["status"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["createdAt"] = aws_sdk_rtbfabric.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["updatedAt"] = aws_sdk_rtbfabric.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    out["port"] = value["port"]
    import aws_sdk_rtbfabric.types.protocol

    out["protocol"] = aws_sdk_rtbfabric.types.protocol.serialize_json(value["protocol"])
    if "listener_config" in value:
        import aws_sdk_rtbfabric.types.listener_config

        out["listenerConfig"] = aws_sdk_rtbfabric.types.listener_config.serialize_json(
            value["listener_config"]
        )
    if "trust_store_configuration" in value:
        import aws_sdk_rtbfabric.types.trust_store_configuration

        out["trustStoreConfiguration"] = (
            aws_sdk_rtbfabric.types.trust_store_configuration.serialize_json(
                value["trust_store_configuration"]
            )
        )
    if "managed_endpoint_configuration" in value:
        import aws_sdk_rtbfabric.types.managed_endpoint_configuration

        out["managedEndpointConfiguration"] = (
            aws_sdk_rtbfabric.types.managed_endpoint_configuration.serialize_json(
                value["managed_endpoint_configuration"]
            )
        )
    out["gatewayId"] = value["gateway_id"]
    if "tags" in value:
        import aws_sdk_rtbfabric.types.tags_map

        out["tags"] = aws_sdk_rtbfabric.types.tags_map.serialize_json(value["tags"])
    if "active_links_count" in value:
        out["activeLinksCount"] = value["active_links_count"]
    if "total_links_count" in value:
        out["totalLinksCount"] = value["total_links_count"]
    if "inbound_links_count" in value:
        out["inboundLinksCount"] = value["inbound_links_count"]
    if "links_requested_count" in value:
        out["linksRequestedCount"] = value["links_requested_count"]
    if "gateway_type" in value:
        import aws_sdk_rtbfabric.types.gateway_type

        out["gatewayType"] = aws_sdk_rtbfabric.types.gateway_type.serialize_json(
            value["gateway_type"]
        )
    if "external_inbound_endpoint" in value:
        out["externalInboundEndpoint"] = value["external_inbound_endpoint"]
    return out


def deserialize_json(data: dict) -> GetResponderGatewayResponse:
    out: GetResponderGatewayResponse = {}  # type: ignore[typeddict-item]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("GetResponderGatewayResponse.vpc_id required")
    if "subnetIds" in data:
        import aws_sdk_rtbfabric.types.subnet_id_list

        out["subnet_ids"] = aws_sdk_rtbfabric.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        raise DeserializationError("GetResponderGatewayResponse.subnet_ids required")
    if "securityGroupIds" in data:
        import aws_sdk_rtbfabric.types.security_group_id_list

        out["security_group_ids"] = (
            aws_sdk_rtbfabric.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "GetResponderGatewayResponse.security_group_ids required"
        )
    if "status" in data:
        import aws_sdk_rtbfabric.types.responder_gateway_status

        out["status"] = (
            aws_sdk_rtbfabric.types.responder_gateway_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetResponderGatewayResponse.status required")
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["created_at"] = aws_sdk_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_rtbfabric.types._prelude.timestamp

        out["updated_at"] = aws_sdk_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "port" in data:
        out["port"] = data["port"]
    else:
        raise DeserializationError("GetResponderGatewayResponse.port required")
    if "protocol" in data:
        import aws_sdk_rtbfabric.types.protocol

        out["protocol"] = aws_sdk_rtbfabric.types.protocol.deserialize_json(
            data["protocol"]
        )
    else:
        raise DeserializationError("GetResponderGatewayResponse.protocol required")
    if "listenerConfig" in data:
        import aws_sdk_rtbfabric.types.listener_config

        out["listener_config"] = (
            aws_sdk_rtbfabric.types.listener_config.deserialize_json(
                data["listenerConfig"]
            )
        )
    if "trustStoreConfiguration" in data:
        import aws_sdk_rtbfabric.types.trust_store_configuration

        out["trust_store_configuration"] = (
            aws_sdk_rtbfabric.types.trust_store_configuration.deserialize_json(
                data["trustStoreConfiguration"]
            )
        )
    if "managedEndpointConfiguration" in data:
        import aws_sdk_rtbfabric.types.managed_endpoint_configuration

        out["managed_endpoint_configuration"] = (
            aws_sdk_rtbfabric.types.managed_endpoint_configuration.deserialize_json(
                data["managedEndpointConfiguration"]
            )
        )
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("GetResponderGatewayResponse.gateway_id required")
    if "tags" in data:
        import aws_sdk_rtbfabric.types.tags_map

        out["tags"] = aws_sdk_rtbfabric.types.tags_map.deserialize_json(data["tags"])
    if "activeLinksCount" in data:
        out["active_links_count"] = data["activeLinksCount"]
    if "totalLinksCount" in data:
        out["total_links_count"] = data["totalLinksCount"]
    if "inboundLinksCount" in data:
        out["inbound_links_count"] = data["inboundLinksCount"]
    if "linksRequestedCount" in data:
        out["links_requested_count"] = data["linksRequestedCount"]
    if "gatewayType" in data:
        import aws_sdk_rtbfabric.types.gateway_type

        out["gateway_type"] = aws_sdk_rtbfabric.types.gateway_type.deserialize_json(
            data["gatewayType"]
        )
    if "externalInboundEndpoint" in data:
        out["external_inbound_endpoint"] = data["externalInboundEndpoint"]
    return out
