"""Generated from Smithy shape ``com.amazonaws.elasticache#IncreaseNodeGroupsInGlobalReplicationGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.boolean
    import aws_sdk_elasticache.types.integer
    import aws_sdk_elasticache.types.regional_configuration_list
    import aws_sdk_elasticache.types.string


class IncreaseNodeGroupsInGlobalReplicationGroupMessage(TypedDict, closed=True):
    global_replication_group_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the Global datastore</p>"""
    node_group_count: NotRequired["aws_sdk_elasticache.types.integer.Integer"]
    """<p>Total number of node groups you want</p>"""
    regional_configurations: NotRequired[
        "aws_sdk_elasticache.types.regional_configuration_list.RegionalConfigurationList"
    ]
    """<p>Describes the replication group IDs, the Amazon regions where they are stored and the shard configuration for each that comprise the Global datastore</p>"""
    apply_immediately: NotRequired["aws_sdk_elasticache.types.boolean.Boolean"]
    """<p>Indicates that the process begins immediately. At present, the only permitted value for this parameter is true.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: IncreaseNodeGroupsInGlobalReplicationGroupMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "global_replication_group_id" in value:
        pairs.append(
            (
                f"{prefix}.GlobalReplicationGroupId",
                str(value["global_replication_group_id"]),
            )
        )
    if "node_group_count" in value:
        pairs.append((f"{prefix}.NodeGroupCount", str(value["node_group_count"])))
    if "regional_configurations" in value:
        import aws_sdk_elasticache.types.regional_configuration_list

        aws_sdk_elasticache.types.regional_configuration_list.serialize_query(
            value["regional_configurations"], pairs, f"{prefix}.RegionalConfigurations"
        )
    if "apply_immediately" in value:
        pairs.append(
            (
                f"{prefix}.ApplyImmediately",
                "true" if value["apply_immediately"] else "false",
            )
        )


def deserialize_query(el: Element) -> IncreaseNodeGroupsInGlobalReplicationGroupMessage:
    out: IncreaseNodeGroupsInGlobalReplicationGroupMessage = {}  # type: ignore[typeddict-item]
    child_global_replication_group_id = el.find("GlobalReplicationGroupId")
    if child_global_replication_group_id is not None:
        out["global_replication_group_id"] = str(
            child_global_replication_group_id.text or ""
        )
    child_node_group_count = el.find("NodeGroupCount")
    if child_node_group_count is not None:
        out["node_group_count"] = int(child_node_group_count.text or "")
    child_regional_configurations = el.find("RegionalConfigurations")
    if child_regional_configurations is not None:
        import aws_sdk_elasticache.types.regional_configuration_list

        out["regional_configurations"] = (
            aws_sdk_elasticache.types.regional_configuration_list.deserialize_query(
                child_regional_configurations
            )
        )
    child_apply_immediately = el.find("ApplyImmediately")
    if child_apply_immediately is not None:
        out["apply_immediately"] = (
            child_apply_immediately.text or ""
        ).lower() == "true"
    return out
