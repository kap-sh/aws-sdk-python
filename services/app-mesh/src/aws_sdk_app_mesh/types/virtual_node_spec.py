"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualNodeSpec``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.backend_defaults
    import aws_sdk_app_mesh.types.backends
    import aws_sdk_app_mesh.types.listeners
    import aws_sdk_app_mesh.types.logging
    import aws_sdk_app_mesh.types.service_discovery


class VirtualNodeSpec(TypedDict, closed=True):
    service_discovery: NotRequired[
        "aws_sdk_app_mesh.types.service_discovery.ServiceDiscovery"
    ]
    """<p>The service discovery information for the virtual node. If your virtual node does not expect ingress traffic, you can omit this parameter. If you specify a <code>listener</code>, then you must specify service discovery information.</p>"""
    listeners: NotRequired["aws_sdk_app_mesh.types.listeners.Listeners"]
    """<p>The listener that the virtual node is expected to receive inbound traffic from. You can specify one listener.</p>"""
    backends: NotRequired["aws_sdk_app_mesh.types.backends.Backends"]
    """<p>The backends that the virtual node is expected to send outbound traffic to.</p>"""
    backend_defaults: NotRequired[
        "aws_sdk_app_mesh.types.backend_defaults.BackendDefaults"
    ]
    """<p>A reference to an object that represents the defaults for backends.</p>"""
    logging: NotRequired["aws_sdk_app_mesh.types.logging.Logging"]
    """<p>The inbound and outbound access logging information for the virtual node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualNodeSpec) -> dict:
    out: dict = {}
    if "service_discovery" in value:
        import aws_sdk_app_mesh.types.service_discovery

        out["serviceDiscovery"] = (
            aws_sdk_app_mesh.types.service_discovery.serialize_json(
                value["service_discovery"]
            )
        )
    if "listeners" in value:
        import aws_sdk_app_mesh.types.listeners

        out["listeners"] = aws_sdk_app_mesh.types.listeners.serialize_json(
            value["listeners"]
        )
    if "backends" in value:
        import aws_sdk_app_mesh.types.backends

        out["backends"] = aws_sdk_app_mesh.types.backends.serialize_json(
            value["backends"]
        )
    if "backend_defaults" in value:
        import aws_sdk_app_mesh.types.backend_defaults

        out["backendDefaults"] = aws_sdk_app_mesh.types.backend_defaults.serialize_json(
            value["backend_defaults"]
        )
    if "logging" in value:
        import aws_sdk_app_mesh.types.logging

        out["logging"] = aws_sdk_app_mesh.types.logging.serialize_json(value["logging"])
    return out


def deserialize_json(data: dict) -> VirtualNodeSpec:
    out: VirtualNodeSpec = {}  # type: ignore[typeddict-item]
    if "serviceDiscovery" in data:
        import aws_sdk_app_mesh.types.service_discovery

        out["service_discovery"] = (
            aws_sdk_app_mesh.types.service_discovery.deserialize_json(
                data["serviceDiscovery"]
            )
        )
    if "listeners" in data:
        import aws_sdk_app_mesh.types.listeners

        out["listeners"] = aws_sdk_app_mesh.types.listeners.deserialize_json(
            data["listeners"]
        )
    if "backends" in data:
        import aws_sdk_app_mesh.types.backends

        out["backends"] = aws_sdk_app_mesh.types.backends.deserialize_json(
            data["backends"]
        )
    if "backendDefaults" in data:
        import aws_sdk_app_mesh.types.backend_defaults

        out["backend_defaults"] = (
            aws_sdk_app_mesh.types.backend_defaults.deserialize_json(
                data["backendDefaults"]
            )
        )
    if "logging" in data:
        import aws_sdk_app_mesh.types.logging

        out["logging"] = aws_sdk_app_mesh.types.logging.deserialize_json(
            data["logging"]
        )
    return out
