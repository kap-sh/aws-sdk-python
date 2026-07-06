"""Generated from Smithy shape ``com.amazonaws.rtbfabric#UpdateResponderGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.domain_name
    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.listener_config
    import aws_sdk_rtbfabric.types.managed_endpoint_configuration
    import aws_sdk_rtbfabric.types.protocol
    import aws_sdk_rtbfabric.types.trust_store_configuration


class UpdateResponderGatewayRequest(TypedDict, closed=True):
    domain_name: NotRequired["aws_sdk_rtbfabric.types.domain_name.DomainName"]
    """<p>The domain name for the responder gateway.</p>"""
    port: "int"
    """<p>The networking port to use.</p>"""
    protocol: "aws_sdk_rtbfabric.types.protocol.Protocol"
    """<p>The networking protocol to use.</p>"""
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
    """<p>The configuration for the managed endpoint.</p>"""
    client_token: "str"
    """<p>The unique client token.</p>"""
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    description: NotRequired["str"]
    """<p>An optional description for the responder gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResponderGatewayRequest) -> dict:
    out: dict = {}
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
    out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateResponderGatewayRequest:
    out: UpdateResponderGatewayRequest = {}  # type: ignore[typeddict-item]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "port" in data:
        out["port"] = data["port"]
    else:
        raise DeserializationError("UpdateResponderGatewayRequest.port required")
    if "protocol" in data:
        import aws_sdk_rtbfabric.types.protocol

        out["protocol"] = aws_sdk_rtbfabric.types.protocol.deserialize_json(
            data["protocol"]
        )
    else:
        raise DeserializationError("UpdateResponderGatewayRequest.protocol required")
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
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "UpdateResponderGatewayRequest.client_token required"
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
