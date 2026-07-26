"""Generated from Smithy shape ``com.amazonaws.appmesh#GrpcRouteMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.grpc_route_metadata

GrpcRouteMetadataList: TypeAlias = list[
    "capo_app_mesh.types.grpc_route_metadata.GrpcRouteMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: GrpcRouteMetadataList) -> list:
    import capo_app_mesh.types.grpc_route_metadata

    out: list = []
    for item in value:
        out.append(capo_app_mesh.types.grpc_route_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> GrpcRouteMetadataList:
    import capo_app_mesh.types.grpc_route_metadata

    out: GrpcRouteMetadataList = []
    for item in data:
        out.append(capo_app_mesh.types.grpc_route_metadata.deserialize_json(item))
    return out
