"""Generated from Smithy shape ``com.amazonaws.elasticache#ReshardingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.allowed_node_group_id
    import capo_elasticache.types.availability_zones_list


class ReshardingConfiguration(TypedDict, closed=True):
    node_group_id: NotRequired[
        "capo_elasticache.types.allowed_node_group_id.AllowedNodeGroupId"
    ]
    """<p>Either the ElastiCache supplied 4-digit id or a user supplied id for the node group these configuration values apply to.</p>"""
    preferred_availability_zones: NotRequired[
        "capo_elasticache.types.availability_zones_list.AvailabilityZonesList"
    ]
    """<p>A list of preferred availability zones for the nodes in this cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReshardingConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "node_group_id" in value:
        pairs.append((f"{prefix}.NodeGroupId", str(value["node_group_id"])))
    if "preferred_availability_zones" in value:
        import capo_elasticache.types.availability_zones_list

        capo_elasticache.types.availability_zones_list.serialize_query(
            value["preferred_availability_zones"],
            pairs,
            f"{prefix}.PreferredAvailabilityZones",
        )


def deserialize_query(el: Element) -> ReshardingConfiguration:
    out: ReshardingConfiguration = {}  # type: ignore[typeddict-item]
    child_node_group_id = el.find("NodeGroupId")
    if child_node_group_id is not None:
        out["node_group_id"] = str(child_node_group_id.text or "")
    child_preferred_availability_zones = el.find("PreferredAvailabilityZones")
    if child_preferred_availability_zones is not None:
        import capo_elasticache.types.availability_zones_list

        out["preferred_availability_zones"] = (
            capo_elasticache.types.availability_zones_list.deserialize_query(
                child_preferred_availability_zones
            )
        )
    return out
