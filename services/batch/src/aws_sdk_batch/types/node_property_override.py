"""Generated from Smithy shape ``com.amazonaws.batch#NodePropertyOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.consumable_resource_properties
    import aws_sdk_batch.types.container_overrides
    import aws_sdk_batch.types.ecs_properties_override
    import aws_sdk_batch.types.eks_properties_override
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.string_list


class NodePropertyOverride(TypedDict, closed=True):
    target_nodes: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The range of nodes, using node index values, that's used to override. A range of <code>0:3</code> indicates nodes with index values of <code>0</code> through <code>3</code>. If the starting range value is omitted (<code>:n</code>), then <code>0</code> is used to start the range. If the ending range value is omitted (<code>n:</code>), then the highest possible node index is used to end the range.</p>"""
    container_overrides: NotRequired[
        "aws_sdk_batch.types.container_overrides.ContainerOverrides"
    ]
    """<p>The overrides that are sent to a node range.</p>"""
    ecs_properties_override: NotRequired[
        "aws_sdk_batch.types.ecs_properties_override.EcsPropertiesOverride"
    ]
    """<p>An object that contains the properties that you want to replace for the existing Amazon ECS resources of a job.</p>"""
    instance_types: NotRequired["aws_sdk_batch.types.string_list.StringList"]
    """<p>An object that contains the instance types that you want to replace for the existing resources of a job.</p>"""
    eks_properties_override: NotRequired[
        "aws_sdk_batch.types.eks_properties_override.EksPropertiesOverride"
    ]
    """<p>An object that contains the properties that you want to replace for the existing Amazon EKS resources of a job.</p>"""
    consumable_resource_properties_override: NotRequired[
        "aws_sdk_batch.types.consumable_resource_properties.ConsumableResourceProperties"
    ]
    """<p>An object that contains overrides for the consumable resources of a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodePropertyOverride) -> dict:
    out: dict = {}
    if "target_nodes" in value:
        out["targetNodes"] = value["target_nodes"]
    if "container_overrides" in value:
        import aws_sdk_batch.types.container_overrides

        out["containerOverrides"] = (
            aws_sdk_batch.types.container_overrides.serialize_json(
                value["container_overrides"]
            )
        )
    if "ecs_properties_override" in value:
        import aws_sdk_batch.types.ecs_properties_override

        out["ecsPropertiesOverride"] = (
            aws_sdk_batch.types.ecs_properties_override.serialize_json(
                value["ecs_properties_override"]
            )
        )
    if "instance_types" in value:
        import aws_sdk_batch.types.string_list

        out["instanceTypes"] = aws_sdk_batch.types.string_list.serialize_json(
            value["instance_types"]
        )
    if "eks_properties_override" in value:
        import aws_sdk_batch.types.eks_properties_override

        out["eksPropertiesOverride"] = (
            aws_sdk_batch.types.eks_properties_override.serialize_json(
                value["eks_properties_override"]
            )
        )
    if "consumable_resource_properties_override" in value:
        import aws_sdk_batch.types.consumable_resource_properties

        out["consumableResourcePropertiesOverride"] = (
            aws_sdk_batch.types.consumable_resource_properties.serialize_json(
                value["consumable_resource_properties_override"]
            )
        )
    return out


def deserialize_json(data: dict) -> NodePropertyOverride:
    out: NodePropertyOverride = {}  # type: ignore[typeddict-item]
    if "targetNodes" in data:
        out["target_nodes"] = data["targetNodes"]
    if "containerOverrides" in data:
        import aws_sdk_batch.types.container_overrides

        out["container_overrides"] = (
            aws_sdk_batch.types.container_overrides.deserialize_json(
                data["containerOverrides"]
            )
        )
    if "ecsPropertiesOverride" in data:
        import aws_sdk_batch.types.ecs_properties_override

        out["ecs_properties_override"] = (
            aws_sdk_batch.types.ecs_properties_override.deserialize_json(
                data["ecsPropertiesOverride"]
            )
        )
    if "instanceTypes" in data:
        import aws_sdk_batch.types.string_list

        out["instance_types"] = aws_sdk_batch.types.string_list.deserialize_json(
            data["instanceTypes"]
        )
    if "eksPropertiesOverride" in data:
        import aws_sdk_batch.types.eks_properties_override

        out["eks_properties_override"] = (
            aws_sdk_batch.types.eks_properties_override.deserialize_json(
                data["eksPropertiesOverride"]
            )
        )
    if "consumableResourcePropertiesOverride" in data:
        import aws_sdk_batch.types.consumable_resource_properties

        out["consumable_resource_properties_override"] = (
            aws_sdk_batch.types.consumable_resource_properties.deserialize_json(
                data["consumableResourcePropertiesOverride"]
            )
        )
    return out
