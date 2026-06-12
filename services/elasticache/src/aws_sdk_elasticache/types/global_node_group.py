"""Generated from Smithy shape ``com.amazonaws.elasticache#GlobalNodeGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string


class GlobalNodeGroup(TypedDict):
    global_node_group_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the global node group</p>"""
    slots: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The keyspace for this node group</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalNodeGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "global_node_group_id" in value:
        pairs.append(
            (f"{prefix}.GlobalNodeGroupId", str(value["global_node_group_id"]))
        )
    if "slots" in value:
        pairs.append((f"{prefix}.Slots", str(value["slots"])))


def deserialize_query(el: Element) -> GlobalNodeGroup:
    out: GlobalNodeGroup = {}  # type: ignore[typeddict-item]
    child_global_node_group_id = el.find("GlobalNodeGroupId")
    if child_global_node_group_id is not None:
        out["global_node_group_id"] = str(child_global_node_group_id.text or "")
    child_slots = el.find("Slots")
    if child_slots is not None:
        out["slots"] = str(child_slots.text or "")
    return out
