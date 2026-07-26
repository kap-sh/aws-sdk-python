"""Generated from Smithy shape ``com.amazonaws.appmesh#Listener``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.health_check_policy
    import capo_app_mesh.types.listener_timeout
    import capo_app_mesh.types.listener_tls
    import capo_app_mesh.types.outlier_detection
    import capo_app_mesh.types.port_mapping
    import capo_app_mesh.types.virtual_node_connection_pool


class Listener(TypedDict, closed=True):
    port_mapping: "capo_app_mesh.types.port_mapping.PortMapping"
    """<p>The port mapping information for the listener.</p>"""
    tls: NotRequired["capo_app_mesh.types.listener_tls.ListenerTls"]
    """<p>A reference to an object that represents the Transport Layer Security (TLS) properties for a listener.</p>"""
    health_check: NotRequired[
        "capo_app_mesh.types.health_check_policy.HealthCheckPolicy"
    ]
    """<p>The health check information for the listener.</p>"""
    timeout: NotRequired["capo_app_mesh.types.listener_timeout.ListenerTimeout"]
    """<p>An object that represents timeouts for different protocols.</p>"""
    outlier_detection: NotRequired[
        "capo_app_mesh.types.outlier_detection.OutlierDetection"
    ]
    """<p>The outlier detection information for the listener.</p>"""
    connection_pool: NotRequired[
        "capo_app_mesh.types.virtual_node_connection_pool.VirtualNodeConnectionPool"
    ]
    """<p>The connection pool information for the listener.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Listener) -> dict:
    out: dict = {}
    import capo_app_mesh.types.port_mapping

    out["portMapping"] = capo_app_mesh.types.port_mapping.serialize_json(
        value["port_mapping"]
    )
    if "tls" in value:
        import capo_app_mesh.types.listener_tls

        out["tls"] = capo_app_mesh.types.listener_tls.serialize_json(value["tls"])
    if "health_check" in value:
        import capo_app_mesh.types.health_check_policy

        out["healthCheck"] = capo_app_mesh.types.health_check_policy.serialize_json(
            value["health_check"]
        )
    if "timeout" in value:
        import capo_app_mesh.types.listener_timeout

        out["timeout"] = capo_app_mesh.types.listener_timeout.serialize_json(
            value["timeout"]
        )
    if "outlier_detection" in value:
        import capo_app_mesh.types.outlier_detection

        out["outlierDetection"] = capo_app_mesh.types.outlier_detection.serialize_json(
            value["outlier_detection"]
        )
    if "connection_pool" in value:
        import capo_app_mesh.types.virtual_node_connection_pool

        out["connectionPool"] = (
            capo_app_mesh.types.virtual_node_connection_pool.serialize_json(
                value["connection_pool"]
            )
        )
    return out


def deserialize_json(data: dict) -> Listener:
    out: Listener = {}  # type: ignore[typeddict-item]
    if "portMapping" in data:
        import capo_app_mesh.types.port_mapping

        out["port_mapping"] = capo_app_mesh.types.port_mapping.deserialize_json(
            data["portMapping"]
        )
    else:
        raise DeserializationError("Listener.port_mapping required")
    if "tls" in data:
        import capo_app_mesh.types.listener_tls

        out["tls"] = capo_app_mesh.types.listener_tls.deserialize_json(data["tls"])
    if "healthCheck" in data:
        import capo_app_mesh.types.health_check_policy

        out["health_check"] = capo_app_mesh.types.health_check_policy.deserialize_json(
            data["healthCheck"]
        )
    if "timeout" in data:
        import capo_app_mesh.types.listener_timeout

        out["timeout"] = capo_app_mesh.types.listener_timeout.deserialize_json(
            data["timeout"]
        )
    if "outlierDetection" in data:
        import capo_app_mesh.types.outlier_detection

        out["outlier_detection"] = (
            capo_app_mesh.types.outlier_detection.deserialize_json(
                data["outlierDetection"]
            )
        )
    if "connectionPool" in data:
        import capo_app_mesh.types.virtual_node_connection_pool

        out["connection_pool"] = (
            capo_app_mesh.types.virtual_node_connection_pool.deserialize_json(
                data["connectionPool"]
            )
        )
    return out
