"""Generated from Smithy shape ``com.amazonaws.appmesh#MeshSpec``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.egress_filter
    import aws_sdk_app_mesh.types.mesh_service_discovery


class MeshSpec(TypedDict):
    egress_filter: NotRequired["aws_sdk_app_mesh.types.egress_filter.EgressFilter"]
    """<p>The egress filter rules for the service mesh.</p>"""
    service_discovery: NotRequired[
        "aws_sdk_app_mesh.types.mesh_service_discovery.MeshServiceDiscovery"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MeshSpec) -> dict:
    out: dict = {}
    if "egress_filter" in value:
        import aws_sdk_app_mesh.types.egress_filter

        out["egressFilter"] = aws_sdk_app_mesh.types.egress_filter.serialize_json(
            value["egress_filter"]
        )
    if "service_discovery" in value:
        import aws_sdk_app_mesh.types.mesh_service_discovery

        out["serviceDiscovery"] = (
            aws_sdk_app_mesh.types.mesh_service_discovery.serialize_json(
                value["service_discovery"]
            )
        )
    return out


def deserialize_json(data: dict) -> MeshSpec:
    out: MeshSpec = {}  # type: ignore[typeddict-item]
    if "egressFilter" in data:
        import aws_sdk_app_mesh.types.egress_filter

        out["egress_filter"] = aws_sdk_app_mesh.types.egress_filter.deserialize_json(
            data["egressFilter"]
        )
    if "serviceDiscovery" in data:
        import aws_sdk_app_mesh.types.mesh_service_discovery

        out["service_discovery"] = (
            aws_sdk_app_mesh.types.mesh_service_discovery.deserialize_json(
                data["serviceDiscovery"]
            )
        )
    return out
