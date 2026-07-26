"""Generated from Smithy shape ``com.amazonaws.opensearch#NodeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean
    import capo_opensearch.types.integer_class
    import capo_opensearch.types.open_search_partition_instance_type


class NodeConfig(TypedDict, closed=True):
    enabled: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>A boolean value indicating whether a specific node type is active or inactive.</p>"""
    type: NotRequired[
        "capo_opensearch.types.open_search_partition_instance_type.OpenSearchPartitionInstanceType"
    ]
    """<p>The instance type of a particular node within the cluster.</p>"""
    count: NotRequired["capo_opensearch.types.integer_class.IntegerClass"]
    """<p>The number of nodes of a specific type within the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeConfig) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "type" in value:
        import capo_opensearch.types.open_search_partition_instance_type

        out["Type"] = (
            capo_opensearch.types.open_search_partition_instance_type.serialize_json(
                value["type"]
            )
        )
    if "count" in value:
        out["Count"] = value["count"]
    return out


def deserialize_json(data: dict) -> NodeConfig:
    out: NodeConfig = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "Type" in data:
        import capo_opensearch.types.open_search_partition_instance_type

        out["type"] = (
            capo_opensearch.types.open_search_partition_instance_type.deserialize_json(
                data["Type"]
            )
        )
    if "Count" in data:
        out["count"] = data["Count"]
    return out
