"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayListener``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_gateway_connection_pool
    import aws_sdk_app_mesh.types.virtual_gateway_health_check_policy
    import aws_sdk_app_mesh.types.virtual_gateway_listener_tls
    import aws_sdk_app_mesh.types.virtual_gateway_port_mapping


class VirtualGatewayListener(TypedDict, closed=True):
    health_check: NotRequired[
        "aws_sdk_app_mesh.types.virtual_gateway_health_check_policy.VirtualGatewayHealthCheckPolicy"
    ]
    """<p>The health check information for the listener.</p>"""
    port_mapping: (
        "aws_sdk_app_mesh.types.virtual_gateway_port_mapping.VirtualGatewayPortMapping"
    )
    """<p>The port mapping information for the listener.</p>"""
    tls: NotRequired[
        "aws_sdk_app_mesh.types.virtual_gateway_listener_tls.VirtualGatewayListenerTls"
    ]
    """<p>A reference to an object that represents the Transport Layer Security (TLS) properties for the listener.</p>"""
    connection_pool: NotRequired[
        "aws_sdk_app_mesh.types.virtual_gateway_connection_pool.VirtualGatewayConnectionPool"
    ]
    """<p>The connection pool information for the virtual gateway listener.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayListener) -> dict:
    out: dict = {}
    if "health_check" in value:
        import aws_sdk_app_mesh.types.virtual_gateway_health_check_policy

        out["healthCheck"] = (
            aws_sdk_app_mesh.types.virtual_gateway_health_check_policy.serialize_json(
                value["health_check"]
            )
        )
    import aws_sdk_app_mesh.types.virtual_gateway_port_mapping

    out["portMapping"] = (
        aws_sdk_app_mesh.types.virtual_gateway_port_mapping.serialize_json(
            value["port_mapping"]
        )
    )
    if "tls" in value:
        import aws_sdk_app_mesh.types.virtual_gateway_listener_tls

        out["tls"] = aws_sdk_app_mesh.types.virtual_gateway_listener_tls.serialize_json(
            value["tls"]
        )
    if "connection_pool" in value:
        import aws_sdk_app_mesh.types.virtual_gateway_connection_pool

        out["connectionPool"] = (
            aws_sdk_app_mesh.types.virtual_gateway_connection_pool.serialize_json(
                value["connection_pool"]
            )
        )
    return out


def deserialize_json(data: dict) -> VirtualGatewayListener:
    out: VirtualGatewayListener = {}  # type: ignore[typeddict-item]
    if "healthCheck" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_health_check_policy

        out["health_check"] = (
            aws_sdk_app_mesh.types.virtual_gateway_health_check_policy.deserialize_json(
                data["healthCheck"]
            )
        )
    if "portMapping" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_port_mapping

        out["port_mapping"] = (
            aws_sdk_app_mesh.types.virtual_gateway_port_mapping.deserialize_json(
                data["portMapping"]
            )
        )
    else:
        raise DeserializationError("VirtualGatewayListener.port_mapping required")
    if "tls" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_listener_tls

        out["tls"] = (
            aws_sdk_app_mesh.types.virtual_gateway_listener_tls.deserialize_json(
                data["tls"]
            )
        )
    if "connectionPool" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_connection_pool

        out["connection_pool"] = (
            aws_sdk_app_mesh.types.virtual_gateway_connection_pool.deserialize_json(
                data["connectionPool"]
            )
        )
    return out
