"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualServiceProvider``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_node_service_provider
    import aws_sdk_app_mesh.types.virtual_router_service_provider


class _VirtualServiceProvider_virtualNode(TypedDict):
    virtualNode: "aws_sdk_app_mesh.types.virtual_node_service_provider.VirtualNodeServiceProvider"


class _VirtualServiceProvider_virtualRouter(TypedDict):
    virtualRouter: "aws_sdk_app_mesh.types.virtual_router_service_provider.VirtualRouterServiceProvider"


VirtualServiceProvider: TypeAlias = (
    _VirtualServiceProvider_virtualNode | _VirtualServiceProvider_virtualRouter
)


# --- restJson1 ser/de ---
def serialize_json(value: VirtualServiceProvider) -> dict:
    if "virtualNode" in value:
        import aws_sdk_app_mesh.types.virtual_node_service_provider

        return {
            "virtualNode": aws_sdk_app_mesh.types.virtual_node_service_provider.serialize_json(
                value["virtualNode"]
            )
        }
    elif "virtualRouter" in value:
        import aws_sdk_app_mesh.types.virtual_router_service_provider

        return {
            "virtualRouter": aws_sdk_app_mesh.types.virtual_router_service_provider.serialize_json(
                value["virtualRouter"]
            )
        }
    else:
        raise SerializationError("VirtualServiceProvider: no variant present")


def deserialize_json(data: dict) -> VirtualServiceProvider:
    if "virtualNode" in data:
        import aws_sdk_app_mesh.types.virtual_node_service_provider

        return {
            "virtualNode": aws_sdk_app_mesh.types.virtual_node_service_provider.deserialize_json(
                data["virtualNode"]
            )
        }
    elif "virtualRouter" in data:
        import aws_sdk_app_mesh.types.virtual_router_service_provider

        return {
            "virtualRouter": aws_sdk_app_mesh.types.virtual_router_service_provider.deserialize_json(
                data["virtualRouter"]
            )
        }
    else:
        raise DeserializationError("VirtualServiceProvider: no recognized variant key")
