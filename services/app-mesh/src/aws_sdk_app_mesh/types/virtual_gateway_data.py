"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayData``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.resource_metadata
    import aws_sdk_app_mesh.types.resource_name
    import aws_sdk_app_mesh.types.virtual_gateway_spec
    import aws_sdk_app_mesh.types.virtual_gateway_status


class VirtualGatewayData(TypedDict):
    mesh_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh that the virtual gateway resides in.</p>"""
    virtual_gateway_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the virtual gateway.</p>"""
    spec: "aws_sdk_app_mesh.types.virtual_gateway_spec.VirtualGatewaySpec"
    """<p>The specifications of the virtual gateway.</p>"""
    metadata: "aws_sdk_app_mesh.types.resource_metadata.ResourceMetadata"
    status: "aws_sdk_app_mesh.types.virtual_gateway_status.VirtualGatewayStatus"
    """<p>The current status of the virtual gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayData) -> dict:
    out: dict = {}
    out["meshName"] = value["mesh_name"]
    out["virtualGatewayName"] = value["virtual_gateway_name"]
    import aws_sdk_app_mesh.types.virtual_gateway_spec

    out["spec"] = aws_sdk_app_mesh.types.virtual_gateway_spec.serialize_json(
        value["spec"]
    )
    import aws_sdk_app_mesh.types.resource_metadata

    out["metadata"] = aws_sdk_app_mesh.types.resource_metadata.serialize_json(
        value["metadata"]
    )
    import aws_sdk_app_mesh.types.virtual_gateway_status

    out["status"] = aws_sdk_app_mesh.types.virtual_gateway_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> VirtualGatewayData:
    out: VirtualGatewayData = {}  # type: ignore[typeddict-item]
    if "meshName" in data:
        out["mesh_name"] = data["meshName"]
    else:
        raise DeserializationError("VirtualGatewayData.mesh_name required")
    if "virtualGatewayName" in data:
        out["virtual_gateway_name"] = data["virtualGatewayName"]
    else:
        raise DeserializationError("VirtualGatewayData.virtual_gateway_name required")
    if "spec" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_spec

        out["spec"] = aws_sdk_app_mesh.types.virtual_gateway_spec.deserialize_json(
            data["spec"]
        )
    else:
        raise DeserializationError("VirtualGatewayData.spec required")
    if "metadata" in data:
        import aws_sdk_app_mesh.types.resource_metadata

        out["metadata"] = aws_sdk_app_mesh.types.resource_metadata.deserialize_json(
            data["metadata"]
        )
    else:
        raise DeserializationError("VirtualGatewayData.metadata required")
    if "status" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_status

        out["status"] = aws_sdk_app_mesh.types.virtual_gateway_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("VirtualGatewayData.status required")
    return out
