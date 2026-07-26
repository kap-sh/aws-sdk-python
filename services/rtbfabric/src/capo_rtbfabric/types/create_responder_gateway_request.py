"""Generated from Smithy shape ``com.amazonaws.rtbfabric#CreateResponderGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.domain_name
    import capo_rtbfabric.types.gateway_type
    import capo_rtbfabric.types.listener_config
    import capo_rtbfabric.types.managed_endpoint_configuration
    import capo_rtbfabric.types.protocol
    import capo_rtbfabric.types.security_group_id_list
    import capo_rtbfabric.types.subnet_id_list
    import capo_rtbfabric.types.tags_map
    import capo_rtbfabric.types.trust_store_configuration
    import capo_rtbfabric.types.vpc_id


class CreateResponderGatewayRequest(TypedDict, closed=True):
    vpc_id: "capo_rtbfabric.types.vpc_id.VpcId"
    """<p>The unique identifier of the Virtual Private Cloud (VPC).</p>"""
    subnet_ids: "capo_rtbfabric.types.subnet_id_list.SubnetIdList"
    """<p>The unique identifiers of the subnets.</p>"""
    security_group_ids: (
        "capo_rtbfabric.types.security_group_id_list.SecurityGroupIdList"
    )
    """<p>The unique identifiers of the security groups.</p>"""
    domain_name: NotRequired["capo_rtbfabric.types.domain_name.DomainName"]
    """<p>The domain name for the responder gateway.</p>"""
    port: "int"
    """<p>The networking port to use.</p>"""
    protocol: "capo_rtbfabric.types.protocol.Protocol"
    """<p>The networking protocol to use.</p>"""
    listener_config: NotRequired["capo_rtbfabric.types.listener_config.ListenerConfig"]
    trust_store_configuration: NotRequired[
        "capo_rtbfabric.types.trust_store_configuration.TrustStoreConfiguration"
    ]
    """<p>The configuration of the trust store.</p>"""
    managed_endpoint_configuration: NotRequired[
        "capo_rtbfabric.types.managed_endpoint_configuration.ManagedEndpointConfiguration"
    ]
    """<p>The configuration for the managed endpoint.</p>"""
    client_token: "str"
    """<p>The unique client token.</p>"""
    description: NotRequired["str"]
    """<p>An optional description for the responder gateway.</p>"""
    tags: NotRequired["capo_rtbfabric.types.tags_map.TagsMap"]
    """<p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>"""
    gateway_type: NotRequired["capo_rtbfabric.types.gateway_type.GatewayType"]
    """<p>The type of gateway. Valid values are <code>EXTERNAL</code> or <code>INTERNAL</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResponderGatewayRequest) -> dict:
    out: dict = {}
    out["vpcId"] = value["vpc_id"]
    import capo_rtbfabric.types.subnet_id_list

    out["subnetIds"] = capo_rtbfabric.types.subnet_id_list.serialize_json(
        value["subnet_ids"]
    )
    import capo_rtbfabric.types.security_group_id_list

    out["securityGroupIds"] = (
        capo_rtbfabric.types.security_group_id_list.serialize_json(
            value["security_group_ids"]
        )
    )
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    out["port"] = value["port"]
    import capo_rtbfabric.types.protocol

    out["protocol"] = capo_rtbfabric.types.protocol.serialize_json(value["protocol"])
    if "listener_config" in value:
        import capo_rtbfabric.types.listener_config

        out["listenerConfig"] = capo_rtbfabric.types.listener_config.serialize_json(
            value["listener_config"]
        )
    if "trust_store_configuration" in value:
        import capo_rtbfabric.types.trust_store_configuration

        out["trustStoreConfiguration"] = (
            capo_rtbfabric.types.trust_store_configuration.serialize_json(
                value["trust_store_configuration"]
            )
        )
    if "managed_endpoint_configuration" in value:
        import capo_rtbfabric.types.managed_endpoint_configuration

        out["managedEndpointConfiguration"] = (
            capo_rtbfabric.types.managed_endpoint_configuration.serialize_json(
                value["managed_endpoint_configuration"]
            )
        )
    out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_rtbfabric.types.tags_map

        out["tags"] = capo_rtbfabric.types.tags_map.serialize_json(value["tags"])
    if "gateway_type" in value:
        import capo_rtbfabric.types.gateway_type

        out["gatewayType"] = capo_rtbfabric.types.gateway_type.serialize_json(
            value["gateway_type"]
        )
    return out


def deserialize_json(data: dict) -> CreateResponderGatewayRequest:
    out: CreateResponderGatewayRequest = {}  # type: ignore[typeddict-item]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("CreateResponderGatewayRequest.vpc_id required")
    if "subnetIds" in data:
        import capo_rtbfabric.types.subnet_id_list

        out["subnet_ids"] = capo_rtbfabric.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        raise DeserializationError("CreateResponderGatewayRequest.subnet_ids required")
    if "securityGroupIds" in data:
        import capo_rtbfabric.types.security_group_id_list

        out["security_group_ids"] = (
            capo_rtbfabric.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "CreateResponderGatewayRequest.security_group_ids required"
        )
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "port" in data:
        out["port"] = data["port"]
    else:
        raise DeserializationError("CreateResponderGatewayRequest.port required")
    if "protocol" in data:
        import capo_rtbfabric.types.protocol

        out["protocol"] = capo_rtbfabric.types.protocol.deserialize_json(
            data["protocol"]
        )
    else:
        raise DeserializationError("CreateResponderGatewayRequest.protocol required")
    if "listenerConfig" in data:
        import capo_rtbfabric.types.listener_config

        out["listener_config"] = capo_rtbfabric.types.listener_config.deserialize_json(
            data["listenerConfig"]
        )
    if "trustStoreConfiguration" in data:
        import capo_rtbfabric.types.trust_store_configuration

        out["trust_store_configuration"] = (
            capo_rtbfabric.types.trust_store_configuration.deserialize_json(
                data["trustStoreConfiguration"]
            )
        )
    if "managedEndpointConfiguration" in data:
        import capo_rtbfabric.types.managed_endpoint_configuration

        out["managed_endpoint_configuration"] = (
            capo_rtbfabric.types.managed_endpoint_configuration.deserialize_json(
                data["managedEndpointConfiguration"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "CreateResponderGatewayRequest.client_token required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import capo_rtbfabric.types.tags_map

        out["tags"] = capo_rtbfabric.types.tags_map.deserialize_json(data["tags"])
    if "gatewayType" in data:
        import capo_rtbfabric.types.gateway_type

        out["gateway_type"] = capo_rtbfabric.types.gateway_type.deserialize_json(
            data["gatewayType"]
        )
    return out
