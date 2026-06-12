"""Generated from Smithy shape ``com.amazonaws.emrcontainers#VirtualCluster``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.container_provider
    import aws_sdk_emr_containers.types.date
    import aws_sdk_emr_containers.types.resource_id_string
    import aws_sdk_emr_containers.types.resource_name_string
    import aws_sdk_emr_containers.types.tag_map
    import aws_sdk_emr_containers.types.virtual_cluster_arn
    import aws_sdk_emr_containers.types.virtual_cluster_state


class VirtualCluster(TypedDict):
    id: NotRequired["aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"]
    """<p>The ID of the virtual cluster.</p>"""
    name: NotRequired[
        "aws_sdk_emr_containers.types.resource_name_string.ResourceNameString"
    ]
    """<p>The name of the virtual cluster.</p>"""
    arn: NotRequired[
        "aws_sdk_emr_containers.types.virtual_cluster_arn.VirtualClusterArn"
    ]
    """<p>The ARN of the virtual cluster.</p>"""
    state: NotRequired[
        "aws_sdk_emr_containers.types.virtual_cluster_state.VirtualClusterState"
    ]
    """<p>The state of the virtual cluster.</p>"""
    container_provider: NotRequired[
        "aws_sdk_emr_containers.types.container_provider.ContainerProvider"
    ]
    """<p>The container provider of the virtual cluster.</p>"""
    created_at: NotRequired["aws_sdk_emr_containers.types.date.Date"]
    """<p>The date and time when the virtual cluster is created.</p>"""
    tags: NotRequired["aws_sdk_emr_containers.types.tag_map.TagMap"]
    """<p>The assigned tags of the virtual cluster.</p>"""
    security_configuration_id: NotRequired[
        "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
    ]
    """<p>The ID of the security configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualCluster) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "state" in value:
        import aws_sdk_emr_containers.types.virtual_cluster_state

        out["state"] = (
            aws_sdk_emr_containers.types.virtual_cluster_state.serialize_json(
                value["state"]
            )
        )
    if "container_provider" in value:
        import aws_sdk_emr_containers.types.container_provider

        out["containerProvider"] = (
            aws_sdk_emr_containers.types.container_provider.serialize_json(
                value["container_provider"]
            )
        )
    if "created_at" in value:
        import aws_sdk_emr_containers.types.date

        out["createdAt"] = aws_sdk_emr_containers.types.date.serialize_json(
            value["created_at"]
        )
    if "tags" in value:
        import aws_sdk_emr_containers.types.tag_map

        out["tags"] = aws_sdk_emr_containers.types.tag_map.serialize_json(value["tags"])
    if "security_configuration_id" in value:
        out["securityConfigurationId"] = value["security_configuration_id"]
    return out


def deserialize_json(data: dict) -> VirtualCluster:
    out: VirtualCluster = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "state" in data:
        import aws_sdk_emr_containers.types.virtual_cluster_state

        out["state"] = (
            aws_sdk_emr_containers.types.virtual_cluster_state.deserialize_json(
                data["state"]
            )
        )
    if "containerProvider" in data:
        import aws_sdk_emr_containers.types.container_provider

        out["container_provider"] = (
            aws_sdk_emr_containers.types.container_provider.deserialize_json(
                data["containerProvider"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_emr_containers.types.date

        out["created_at"] = aws_sdk_emr_containers.types.date.deserialize_json(
            data["createdAt"]
        )
    if "tags" in data:
        import aws_sdk_emr_containers.types.tag_map

        out["tags"] = aws_sdk_emr_containers.types.tag_map.deserialize_json(
            data["tags"]
        )
    if "securityConfigurationId" in data:
        out["security_configuration_id"] = data["securityConfigurationId"]
    return out
