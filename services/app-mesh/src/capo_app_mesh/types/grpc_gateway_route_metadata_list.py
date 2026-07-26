"""Generated from Smithy shape ``com.amazonaws.appmesh#GrpcGatewayRouteMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.grpc_gateway_route_metadata

GrpcGatewayRouteMetadataList: TypeAlias = list[
    "capo_app_mesh.types.grpc_gateway_route_metadata.GrpcGatewayRouteMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: GrpcGatewayRouteMetadataList) -> list:
    import capo_app_mesh.types.grpc_gateway_route_metadata

    out: list = []
    for item in value:
        out.append(capo_app_mesh.types.grpc_gateway_route_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> GrpcGatewayRouteMetadataList:
    import capo_app_mesh.types.grpc_gateway_route_metadata

    out: GrpcGatewayRouteMetadataList = []
    for item in data:
        out.append(
            capo_app_mesh.types.grpc_gateway_route_metadata.deserialize_json(item)
        )
    return out
