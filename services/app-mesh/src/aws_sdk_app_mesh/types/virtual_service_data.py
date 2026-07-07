"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualServiceData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.resource_metadata
    import aws_sdk_app_mesh.types.resource_name
    import aws_sdk_app_mesh.types.service_name
    import aws_sdk_app_mesh.types.virtual_service_spec
    import aws_sdk_app_mesh.types.virtual_service_status


class VirtualServiceData(TypedDict, closed=True):
    mesh_name: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the service mesh that the virtual service resides in.</p>"""
    virtual_service_name: "aws_sdk_app_mesh.types.service_name.ServiceName"
    """<p>The name of the virtual service.</p>"""
    spec: "aws_sdk_app_mesh.types.virtual_service_spec.VirtualServiceSpec"
    """<p>The specifications of the virtual service.</p>"""
    metadata: "aws_sdk_app_mesh.types.resource_metadata.ResourceMetadata"
    status: "aws_sdk_app_mesh.types.virtual_service_status.VirtualServiceStatus"
    """<p>The current status of the virtual service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualServiceData) -> dict:
    out: dict = {}
    out["meshName"] = value["mesh_name"]
    out["virtualServiceName"] = value["virtual_service_name"]
    import aws_sdk_app_mesh.types.virtual_service_spec

    out["spec"] = aws_sdk_app_mesh.types.virtual_service_spec.serialize_json(
        value["spec"]
    )
    import aws_sdk_app_mesh.types.resource_metadata

    out["metadata"] = aws_sdk_app_mesh.types.resource_metadata.serialize_json(
        value["metadata"]
    )
    import aws_sdk_app_mesh.types.virtual_service_status

    out["status"] = aws_sdk_app_mesh.types.virtual_service_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> VirtualServiceData:
    out: VirtualServiceData = {}  # type: ignore[typeddict-item]
    if "meshName" in data:
        out["mesh_name"] = data["meshName"]
    else:
        raise DeserializationError("VirtualServiceData.mesh_name required")
    if "virtualServiceName" in data:
        out["virtual_service_name"] = data["virtualServiceName"]
    else:
        raise DeserializationError("VirtualServiceData.virtual_service_name required")
    if "spec" in data:
        import aws_sdk_app_mesh.types.virtual_service_spec

        out["spec"] = aws_sdk_app_mesh.types.virtual_service_spec.deserialize_json(
            data["spec"]
        )
    else:
        raise DeserializationError("VirtualServiceData.spec required")
    if "metadata" in data:
        import aws_sdk_app_mesh.types.resource_metadata

        out["metadata"] = aws_sdk_app_mesh.types.resource_metadata.deserialize_json(
            data["metadata"]
        )
    else:
        raise DeserializationError("VirtualServiceData.metadata required")
    if "status" in data:
        import aws_sdk_app_mesh.types.virtual_service_status

        out["status"] = aws_sdk_app_mesh.types.virtual_service_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("VirtualServiceData.status required")
    return out
