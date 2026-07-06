"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewaySpec``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_gateway_backend_defaults
    import aws_sdk_app_mesh.types.virtual_gateway_listeners
    import aws_sdk_app_mesh.types.virtual_gateway_logging


class VirtualGatewaySpec(TypedDict, closed=True):
    backend_defaults: NotRequired[
        "aws_sdk_app_mesh.types.virtual_gateway_backend_defaults.VirtualGatewayBackendDefaults"
    ]
    """<p>A reference to an object that represents the defaults for backends.</p>"""
    listeners: (
        "aws_sdk_app_mesh.types.virtual_gateway_listeners.VirtualGatewayListeners"
    )
    """<p>The listeners that the mesh endpoint is expected to receive inbound traffic from. You can specify one listener.</p>"""
    logging: NotRequired[
        "aws_sdk_app_mesh.types.virtual_gateway_logging.VirtualGatewayLogging"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewaySpec) -> dict:
    out: dict = {}
    if "backend_defaults" in value:
        import aws_sdk_app_mesh.types.virtual_gateway_backend_defaults

        out["backendDefaults"] = (
            aws_sdk_app_mesh.types.virtual_gateway_backend_defaults.serialize_json(
                value["backend_defaults"]
            )
        )
    import aws_sdk_app_mesh.types.virtual_gateway_listeners

    out["listeners"] = aws_sdk_app_mesh.types.virtual_gateway_listeners.serialize_json(
        value["listeners"]
    )
    if "logging" in value:
        import aws_sdk_app_mesh.types.virtual_gateway_logging

        out["logging"] = aws_sdk_app_mesh.types.virtual_gateway_logging.serialize_json(
            value["logging"]
        )
    return out


def deserialize_json(data: dict) -> VirtualGatewaySpec:
    out: VirtualGatewaySpec = {}  # type: ignore[typeddict-item]
    if "backendDefaults" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_backend_defaults

        out["backend_defaults"] = (
            aws_sdk_app_mesh.types.virtual_gateway_backend_defaults.deserialize_json(
                data["backendDefaults"]
            )
        )
    if "listeners" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_listeners

        out["listeners"] = (
            aws_sdk_app_mesh.types.virtual_gateway_listeners.deserialize_json(
                data["listeners"]
            )
        )
    else:
        raise DeserializationError("VirtualGatewaySpec.listeners required")
    if "logging" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_logging

        out["logging"] = (
            aws_sdk_app_mesh.types.virtual_gateway_logging.deserialize_json(
                data["logging"]
            )
        )
    return out
