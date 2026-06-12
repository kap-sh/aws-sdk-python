"""Generated from Smithy shape ``com.amazonaws.elasticache#TestMigrationMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.customer_node_endpoint_list
    import aws_sdk_elasticache.types.string


class TestMigrationMessage(TypedDict):
    replication_group_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p> The ID of the replication group to which data is to be migrated. </p>"""
    customer_node_endpoint_list: NotRequired[
        "aws_sdk_elasticache.types.customer_node_endpoint_list.CustomerNodeEndpointList"
    ]
    """<p> List of endpoints from which data should be migrated. List should have only one element. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TestMigrationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "replication_group_id" in value:
        pairs.append(
            (f"{prefix}.ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "customer_node_endpoint_list" in value:
        import aws_sdk_elasticache.types.customer_node_endpoint_list

        aws_sdk_elasticache.types.customer_node_endpoint_list.serialize_query(
            value["customer_node_endpoint_list"],
            pairs,
            f"{prefix}.CustomerNodeEndpointList",
        )


def deserialize_query(el: Element) -> TestMigrationMessage:
    out: TestMigrationMessage = {}  # type: ignore[typeddict-item]
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_customer_node_endpoint_list = el.find("CustomerNodeEndpointList")
    if child_customer_node_endpoint_list is not None:
        import aws_sdk_elasticache.types.customer_node_endpoint_list

        out["customer_node_endpoint_list"] = (
            aws_sdk_elasticache.types.customer_node_endpoint_list.deserialize_query(
                child_customer_node_endpoint_list
            )
        )
    return out
