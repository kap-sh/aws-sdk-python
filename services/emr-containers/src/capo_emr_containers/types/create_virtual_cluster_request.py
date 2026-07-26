"""Generated from Smithy shape ``com.amazonaws.emrcontainers#CreateVirtualClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_emr_containers.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_containers.types.client_token
    import capo_emr_containers.types.container_provider
    import capo_emr_containers.types.resource_id_string
    import capo_emr_containers.types.resource_name_string
    import capo_emr_containers.types.tag_map


class CreateVirtualClusterRequest(TypedDict, closed=True):
    name: "capo_emr_containers.types.resource_name_string.ResourceNameString"
    """<p>The specified name of the virtual cluster.</p>"""
    container_provider: "capo_emr_containers.types.container_provider.ContainerProvider"
    """<p>The container provider of the virtual cluster.</p>"""
    client_token: "capo_emr_containers.types.client_token.ClientToken"
    """<p>The client token of the virtual cluster.</p>"""
    tags: NotRequired["capo_emr_containers.types.tag_map.TagMap"]
    """<p>The tags assigned to the virtual cluster.</p>"""
    security_configuration_id: NotRequired[
        "capo_emr_containers.types.resource_id_string.ResourceIdString"
    ]
    """<p>The ID of the security configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVirtualClusterRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_emr_containers.types.container_provider

    out["containerProvider"] = (
        capo_emr_containers.types.container_provider.serialize_json(
            value["container_provider"]
        )
    )
    out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_emr_containers.types.tag_map

        out["tags"] = capo_emr_containers.types.tag_map.serialize_json(value["tags"])
    if "security_configuration_id" in value:
        out["securityConfigurationId"] = value["security_configuration_id"]
    return out


def deserialize_json(data: dict) -> CreateVirtualClusterRequest:
    out: CreateVirtualClusterRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateVirtualClusterRequest.name required")
    if "containerProvider" in data:
        import capo_emr_containers.types.container_provider

        out["container_provider"] = (
            capo_emr_containers.types.container_provider.deserialize_json(
                data["containerProvider"]
            )
        )
    else:
        raise DeserializationError(
            "CreateVirtualClusterRequest.container_provider required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateVirtualClusterRequest.client_token required")
    if "tags" in data:
        import capo_emr_containers.types.tag_map

        out["tags"] = capo_emr_containers.types.tag_map.deserialize_json(data["tags"])
    if "securityConfigurationId" in data:
        out["security_configuration_id"] = data["securityConfigurationId"]
    return out
