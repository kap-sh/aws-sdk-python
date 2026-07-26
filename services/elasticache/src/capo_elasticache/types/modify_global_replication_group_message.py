"""Generated from Smithy shape ``com.amazonaws.elasticache#ModifyGlobalReplicationGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.boolean
    import capo_elasticache.types.boolean_optional
    import capo_elasticache.types.string


class ModifyGlobalReplicationGroupMessage(TypedDict, closed=True):
    global_replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the Global datastore</p>"""
    apply_immediately: NotRequired["capo_elasticache.types.boolean.Boolean"]
    """<p>This parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible. Modifications to Global Replication Groups cannot be requested to be applied in PreferredMaintenceWindow. </p>"""
    cache_node_type: NotRequired["capo_elasticache.types.string.String"]
    """<p>A valid cache node type that you want to scale this Global datastore to.</p>"""
    engine: NotRequired["capo_elasticache.types.string.String"]
    """<p>Modifies the engine listed in a global replication group message. The options are valkey, memcached or redis.</p>"""
    engine_version: NotRequired["capo_elasticache.types.string.String"]
    """<p>The upgraded version of the cache engine to be run on the clusters in the Global datastore. </p>"""
    cache_parameter_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache parameter group to use with the Global datastore. It must be compatible with the major engine version used by the Global datastore.</p>"""
    global_replication_group_description: NotRequired[
        "capo_elasticache.types.string.String"
    ]
    """<p>A description of the Global datastore</p>"""
    automatic_failover_enabled: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>Determines whether a read replica is automatically promoted to read/write primary if the existing primary encounters a failure. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyGlobalReplicationGroupMessage,
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
    if "apply_immediately" in value:
        pairs.append(
            (
                f"{prefix}.ApplyImmediately",
                "true" if value["apply_immediately"] else "false",
            )
        )
    if "cache_node_type" in value:
        pairs.append((f"{prefix}.CacheNodeType", str(value["cache_node_type"])))
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{prefix}.EngineVersion", str(value["engine_version"])))
    if "cache_parameter_group_name" in value:
        pairs.append(
            (
                f"{prefix}.CacheParameterGroupName",
                str(value["cache_parameter_group_name"]),
            )
        )
    if "global_replication_group_description" in value:
        pairs.append(
            (
                f"{prefix}.GlobalReplicationGroupDescription",
                str(value["global_replication_group_description"]),
            )
        )
    if "automatic_failover_enabled" in value:
        pairs.append(
            (
                f"{prefix}.AutomaticFailoverEnabled",
                "true" if value["automatic_failover_enabled"] else "false",
            )
        )


def deserialize_query(el: Element) -> ModifyGlobalReplicationGroupMessage:
    out: ModifyGlobalReplicationGroupMessage = {}  # type: ignore[typeddict-item]
    child_global_replication_group_id = el.find("GlobalReplicationGroupId")
    if child_global_replication_group_id is not None:
        out["global_replication_group_id"] = str(
            child_global_replication_group_id.text or ""
        )
    child_apply_immediately = el.find("ApplyImmediately")
    if child_apply_immediately is not None:
        out["apply_immediately"] = (
            child_apply_immediately.text or ""
        ).lower() == "true"
    child_cache_node_type = el.find("CacheNodeType")
    if child_cache_node_type is not None:
        out["cache_node_type"] = str(child_cache_node_type.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_cache_parameter_group_name = el.find("CacheParameterGroupName")
    if child_cache_parameter_group_name is not None:
        out["cache_parameter_group_name"] = str(
            child_cache_parameter_group_name.text or ""
        )
    child_global_replication_group_description = el.find(
        "GlobalReplicationGroupDescription"
    )
    if child_global_replication_group_description is not None:
        out["global_replication_group_description"] = str(
            child_global_replication_group_description.text or ""
        )
    child_automatic_failover_enabled = el.find("AutomaticFailoverEnabled")
    if child_automatic_failover_enabled is not None:
        out["automatic_failover_enabled"] = (
            child_automatic_failover_enabled.text or ""
        ).lower() == "true"
    return out
