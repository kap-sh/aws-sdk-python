"""Generated from Smithy shape ``com.amazonaws.batch#NodeRangeProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.consumable_resource_properties
    import capo_batch.types.container_properties
    import capo_batch.types.ecs_properties
    import capo_batch.types.eks_properties
    import capo_batch.types.string
    import capo_batch.types.string_list


class NodeRangeProperty(TypedDict, closed=True):
    target_nodes: NotRequired["capo_batch.types.string.String"]
    """<p>The range of nodes, using node index values. A range of <code>0:3</code> indicates nodes with index values of <code>0</code> through <code>3</code>. If the starting range value is omitted (<code>:n</code>), then <code>0</code> is used to start the range. If the ending range value is omitted (<code>n:</code>), then the highest possible node index is used to end the range. Your accumulative node ranges must account for all nodes (<code>0:n</code>). You can nest node ranges (for example, <code>0:10</code> and <code>4:5</code>). In this case, the <code>4:5</code> range properties override the <code>0:10</code> properties.</p>"""
    container: NotRequired["capo_batch.types.container_properties.ContainerProperties"]
    """<p>The container details for the node range.</p>"""
    instance_types: NotRequired["capo_batch.types.string_list.StringList"]
    """<p>The instance types of the underlying host infrastructure of a multi-node parallel job.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources.</p> <p>In addition, this list object is currently limited to one element.</p> </note>"""
    ecs_properties: NotRequired["capo_batch.types.ecs_properties.EcsProperties"]
    """<p>This is an object that represents the properties of the node range for a multi-node parallel job.</p>"""
    eks_properties: NotRequired["capo_batch.types.eks_properties.EksProperties"]
    """<p>This is an object that represents the properties of the node range for a multi-node parallel job.</p>"""
    consumable_resource_properties: NotRequired[
        "capo_batch.types.consumable_resource_properties.ConsumableResourceProperties"
    ]
    """<p>Contains a list of consumable resources required by a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeRangeProperty) -> dict:
    out: dict = {}
    if "target_nodes" in value:
        out["targetNodes"] = value["target_nodes"]
    if "container" in value:
        import capo_batch.types.container_properties

        out["container"] = capo_batch.types.container_properties.serialize_json(
            value["container"]
        )
    if "instance_types" in value:
        import capo_batch.types.string_list

        out["instanceTypes"] = capo_batch.types.string_list.serialize_json(
            value["instance_types"]
        )
    if "ecs_properties" in value:
        import capo_batch.types.ecs_properties

        out["ecsProperties"] = capo_batch.types.ecs_properties.serialize_json(
            value["ecs_properties"]
        )
    if "eks_properties" in value:
        import capo_batch.types.eks_properties

        out["eksProperties"] = capo_batch.types.eks_properties.serialize_json(
            value["eks_properties"]
        )
    if "consumable_resource_properties" in value:
        import capo_batch.types.consumable_resource_properties

        out["consumableResourceProperties"] = (
            capo_batch.types.consumable_resource_properties.serialize_json(
                value["consumable_resource_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> NodeRangeProperty:
    out: NodeRangeProperty = {}  # type: ignore[typeddict-item]
    if "targetNodes" in data:
        out["target_nodes"] = data["targetNodes"]
    if "container" in data:
        import capo_batch.types.container_properties

        out["container"] = capo_batch.types.container_properties.deserialize_json(
            data["container"]
        )
    if "instanceTypes" in data:
        import capo_batch.types.string_list

        out["instance_types"] = capo_batch.types.string_list.deserialize_json(
            data["instanceTypes"]
        )
    if "ecsProperties" in data:
        import capo_batch.types.ecs_properties

        out["ecs_properties"] = capo_batch.types.ecs_properties.deserialize_json(
            data["ecsProperties"]
        )
    if "eksProperties" in data:
        import capo_batch.types.eks_properties

        out["eks_properties"] = capo_batch.types.eks_properties.deserialize_json(
            data["eksProperties"]
        )
    if "consumableResourceProperties" in data:
        import capo_batch.types.consumable_resource_properties

        out["consumable_resource_properties"] = (
            capo_batch.types.consumable_resource_properties.deserialize_json(
                data["consumableResourceProperties"]
            )
        )
    return out
