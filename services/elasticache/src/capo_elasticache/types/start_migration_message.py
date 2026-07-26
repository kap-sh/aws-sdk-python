"""Generated from Smithy shape ``com.amazonaws.elasticache#StartMigrationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.customer_node_endpoint_list
    import capo_elasticache.types.string


class StartMigrationMessage(TypedDict, closed=True):
    replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ID of the replication group to which data should be migrated.</p>"""
    customer_node_endpoint_list: NotRequired[
        "capo_elasticache.types.customer_node_endpoint_list.CustomerNodeEndpointList"
    ]
    """<p>List of endpoints from which data should be migrated. For Valkey or Redis OSS (cluster mode disabled), the list should have only one element.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StartMigrationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "replication_group_id" in value:
        pairs.append(
            (f"{prefix}.ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "customer_node_endpoint_list" in value:
        import capo_elasticache.types.customer_node_endpoint_list

        capo_elasticache.types.customer_node_endpoint_list.serialize_query(
            value["customer_node_endpoint_list"],
            pairs,
            f"{prefix}.CustomerNodeEndpointList",
        )


def deserialize_query(el: Element) -> StartMigrationMessage:
    out: StartMigrationMessage = {}  # type: ignore[typeddict-item]
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_customer_node_endpoint_list = el.find("CustomerNodeEndpointList")
    if child_customer_node_endpoint_list is not None:
        import capo_elasticache.types.customer_node_endpoint_list

        out["customer_node_endpoint_list"] = (
            capo_elasticache.types.customer_node_endpoint_list.deserialize_query(
                child_customer_node_endpoint_list
            )
        )
    return out
