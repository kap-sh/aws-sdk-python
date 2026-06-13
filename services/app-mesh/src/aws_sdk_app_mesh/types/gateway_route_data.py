"""Generated from Smithy shape ``com.amazonaws.appmesh#GatewayRouteData``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.gateway_route_spec
    import aws_sdk_app_mesh.types.gateway_route_status
    import aws_sdk_app_mesh.types.resource_metadata
    import aws_sdk_app_mesh.types.resource_name


class GatewayRouteData(TypedDict):
    mesh_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh that the resource resides in. </p>"""
    gateway_route_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the gateway route.</p>"""
    virtual_gateway_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The virtual gateway that the gateway route is associated with.</p>"""
    spec: "aws_sdk_app_mesh.types.gateway_route_spec.GatewayRouteSpec"
    """<p>The specifications of the gateway route.</p>"""
    metadata: "aws_sdk_app_mesh.types.resource_metadata.ResourceMetadata"
    status: "aws_sdk_app_mesh.types.gateway_route_status.GatewayRouteStatus"
    """<p>The status of the gateway route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayRouteData) -> dict:
    out: dict = {}
    out["meshName"] = value["mesh_name"]
    out["gatewayRouteName"] = value["gateway_route_name"]
    out["virtualGatewayName"] = value["virtual_gateway_name"]
    import aws_sdk_app_mesh.types.gateway_route_spec

    out["spec"] = aws_sdk_app_mesh.types.gateway_route_spec.serialize_json(
        value["spec"]
    )
    import aws_sdk_app_mesh.types.resource_metadata

    out["metadata"] = aws_sdk_app_mesh.types.resource_metadata.serialize_json(
        value["metadata"]
    )
    import aws_sdk_app_mesh.types.gateway_route_status

    out["status"] = aws_sdk_app_mesh.types.gateway_route_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> GatewayRouteData:
    out: GatewayRouteData = {}  # type: ignore[typeddict-item]
    if "meshName" in data:
        out["mesh_name"] = data["meshName"]
    else:
        raise DeserializationError("GatewayRouteData.mesh_name required")
    if "gatewayRouteName" in data:
        out["gateway_route_name"] = data["gatewayRouteName"]
    else:
        raise DeserializationError("GatewayRouteData.gateway_route_name required")
    if "virtualGatewayName" in data:
        out["virtual_gateway_name"] = data["virtualGatewayName"]
    else:
        raise DeserializationError("GatewayRouteData.virtual_gateway_name required")
    if "spec" in data:
        import aws_sdk_app_mesh.types.gateway_route_spec

        out["spec"] = aws_sdk_app_mesh.types.gateway_route_spec.deserialize_json(
            data["spec"]
        )
    else:
        raise DeserializationError("GatewayRouteData.spec required")
    if "metadata" in data:
        import aws_sdk_app_mesh.types.resource_metadata

        out["metadata"] = aws_sdk_app_mesh.types.resource_metadata.deserialize_json(
            data["metadata"]
        )
    else:
        raise DeserializationError("GatewayRouteData.metadata required")
    if "status" in data:
        import aws_sdk_app_mesh.types.gateway_route_status

        out["status"] = aws_sdk_app_mesh.types.gateway_route_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GatewayRouteData.status required")
    return out
