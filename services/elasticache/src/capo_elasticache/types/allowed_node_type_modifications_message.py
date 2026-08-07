"""Generated from Smithy shape ``com.amazonaws.elasticache#AllowedNodeTypeModificationsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.node_type_list


class AllowedNodeTypeModificationsMessage(TypedDict, closed=True):
    scale_up_modifications: NotRequired[
        "capo_elasticache.types.node_type_list.NodeTypeList"
    ]
    """<p>A string list, each element of which specifies a cache node type which you can use to scale your cluster or replication group.</p> <p>When scaling up a Valkey or Redis OSS cluster or replication group using <code>ModifyCacheCluster</code> or <code>ModifyReplicationGroup</code>, use a value from this list for the <code>CacheNodeType</code> parameter.</p>"""
    scale_down_modifications: NotRequired[
        "capo_elasticache.types.node_type_list.NodeTypeList"
    ]
    """<p>A string list, each element of which specifies a cache node type which you can use to scale your cluster or replication group. When scaling down a Valkey or Redis OSS cluster or replication group using ModifyCacheCluster or ModifyReplicationGroup, use a value from this list for the CacheNodeType parameter. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AllowedNodeTypeModificationsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "scale_up_modifications" in value:
        import capo_elasticache.types.node_type_list

        capo_elasticache.types.node_type_list.serialize_query(
            value["scale_up_modifications"], pairs, f"{key_prefix}ScaleUpModifications"
        )
    if "scale_down_modifications" in value:
        import capo_elasticache.types.node_type_list

        capo_elasticache.types.node_type_list.serialize_query(
            value["scale_down_modifications"],
            pairs,
            f"{key_prefix}ScaleDownModifications",
        )


def deserialize_query(el: Element) -> AllowedNodeTypeModificationsMessage:
    out: AllowedNodeTypeModificationsMessage = {}  # type: ignore[typeddict-item]
    child_scale_up_modifications = el.find("ScaleUpModifications")
    if child_scale_up_modifications is not None:
        import capo_elasticache.types.node_type_list

        out["scale_up_modifications"] = (
            capo_elasticache.types.node_type_list.deserialize_query(
                child_scale_up_modifications
            )
        )
    child_scale_down_modifications = el.find("ScaleDownModifications")
    if child_scale_down_modifications is not None:
        import capo_elasticache.types.node_type_list

        out["scale_down_modifications"] = (
            capo_elasticache.types.node_type_list.deserialize_query(
                child_scale_down_modifications
            )
        )
    return out
