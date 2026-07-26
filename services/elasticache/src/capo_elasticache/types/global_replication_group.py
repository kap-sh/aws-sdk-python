"""Generated from Smithy shape ``com.amazonaws.elasticache#GlobalReplicationGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.boolean_optional
    import capo_elasticache.types.global_node_group_list
    import capo_elasticache.types.global_replication_group_member_list
    import capo_elasticache.types.string


class GlobalReplicationGroup(TypedDict, closed=True):
    global_replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the Global datastore</p>"""
    global_replication_group_description: NotRequired[
        "capo_elasticache.types.string.String"
    ]
    """<p>The optional description of the Global datastore</p>"""
    status: NotRequired["capo_elasticache.types.string.String"]
    """<p>The status of the Global datastore</p>"""
    cache_node_type: NotRequired["capo_elasticache.types.string.String"]
    """<p>The cache node type of the Global datastore</p>"""
    engine: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ElastiCache engine. For Valkey or Redis OSS only.</p>"""
    engine_version: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ElastiCache engine version.</p>"""
    members: NotRequired[
        "capo_elasticache.types.global_replication_group_member_list.GlobalReplicationGroupMemberList"
    ]
    """<p>The replication groups that comprise the Global datastore.</p>"""
    cluster_enabled: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>A flag that indicates whether the Global datastore is cluster enabled.</p>"""
    global_node_groups: NotRequired[
        "capo_elasticache.types.global_node_group_list.GlobalNodeGroupList"
    ]
    """<p>Indicates the slot configuration and global identifier for each slice group.</p>"""
    auth_token_enabled: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>A flag that enables using an <code>AuthToken</code> (password) when issuing Valkey or Redis OSS commands.</p> <p>Default: <code>false</code> </p>"""
    transit_encryption_enabled: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>A flag that enables in-transit encryption when set to true.</p> <p> <b>Required:</b> Only available when creating a replication group in an Amazon VPC using Redis OSS version <code>3.2.6</code>, <code>4.x</code> or later.</p>"""
    at_rest_encryption_enabled: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>A flag that enables encryption at rest when set to <code>true</code>.</p> <p>You cannot modify the value of <code>AtRestEncryptionEnabled</code> after the replication group is created. To enable encryption at rest on a replication group you must set <code>AtRestEncryptionEnabled</code> to <code>true</code> when you create the replication group. </p> <p> <b>Required:</b> Only available when creating a replication group in an Amazon VPC using Redis OSS version <code>3.2.6</code>, <code>4.x</code> or later.</p>"""
    arn: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ARN (Amazon Resource Name) of the global replication group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalReplicationGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "global_replication_group_id" in value:
        pairs.append(
            (
                f"{prefix}.GlobalReplicationGroupId",
                str(value["global_replication_group_id"]),
            )
        )
    if "global_replication_group_description" in value:
        pairs.append(
            (
                f"{prefix}.GlobalReplicationGroupDescription",
                str(value["global_replication_group_description"]),
            )
        )
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "cache_node_type" in value:
        pairs.append((f"{prefix}.CacheNodeType", str(value["cache_node_type"])))
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{prefix}.EngineVersion", str(value["engine_version"])))
    if "members" in value:
        import capo_elasticache.types.global_replication_group_member_list

        capo_elasticache.types.global_replication_group_member_list.serialize_query(
            value["members"], pairs, f"{prefix}.Members"
        )
    if "cluster_enabled" in value:
        pairs.append(
            (
                f"{prefix}.ClusterEnabled",
                "true" if value["cluster_enabled"] else "false",
            )
        )
    if "global_node_groups" in value:
        import capo_elasticache.types.global_node_group_list

        capo_elasticache.types.global_node_group_list.serialize_query(
            value["global_node_groups"], pairs, f"{prefix}.GlobalNodeGroups"
        )
    if "auth_token_enabled" in value:
        pairs.append(
            (
                f"{prefix}.AuthTokenEnabled",
                "true" if value["auth_token_enabled"] else "false",
            )
        )
    if "transit_encryption_enabled" in value:
        pairs.append(
            (
                f"{prefix}.TransitEncryptionEnabled",
                "true" if value["transit_encryption_enabled"] else "false",
            )
        )
    if "at_rest_encryption_enabled" in value:
        pairs.append(
            (
                f"{prefix}.AtRestEncryptionEnabled",
                "true" if value["at_rest_encryption_enabled"] else "false",
            )
        )
    if "arn" in value:
        pairs.append((f"{prefix}.ARN", str(value["arn"])))


def deserialize_query(el: Element) -> GlobalReplicationGroup:
    out: GlobalReplicationGroup = {}  # type: ignore[typeddict-item]
    child_global_replication_group_id = el.find("GlobalReplicationGroupId")
    if child_global_replication_group_id is not None:
        out["global_replication_group_id"] = str(
            child_global_replication_group_id.text or ""
        )
    child_global_replication_group_description = el.find(
        "GlobalReplicationGroupDescription"
    )
    if child_global_replication_group_description is not None:
        out["global_replication_group_description"] = str(
            child_global_replication_group_description.text or ""
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_cache_node_type = el.find("CacheNodeType")
    if child_cache_node_type is not None:
        out["cache_node_type"] = str(child_cache_node_type.text or "")
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_members = el.find("Members")
    if child_members is not None:
        import capo_elasticache.types.global_replication_group_member_list

        out["members"] = (
            capo_elasticache.types.global_replication_group_member_list.deserialize_query(
                child_members
            )
        )
    child_cluster_enabled = el.find("ClusterEnabled")
    if child_cluster_enabled is not None:
        out["cluster_enabled"] = (child_cluster_enabled.text or "").lower() == "true"
    child_global_node_groups = el.find("GlobalNodeGroups")
    if child_global_node_groups is not None:
        import capo_elasticache.types.global_node_group_list

        out["global_node_groups"] = (
            capo_elasticache.types.global_node_group_list.deserialize_query(
                child_global_node_groups
            )
        )
    child_auth_token_enabled = el.find("AuthTokenEnabled")
    if child_auth_token_enabled is not None:
        out["auth_token_enabled"] = (
            child_auth_token_enabled.text or ""
        ).lower() == "true"
    child_transit_encryption_enabled = el.find("TransitEncryptionEnabled")
    if child_transit_encryption_enabled is not None:
        out["transit_encryption_enabled"] = (
            child_transit_encryption_enabled.text or ""
        ).lower() == "true"
    child_at_rest_encryption_enabled = el.find("AtRestEncryptionEnabled")
    if child_at_rest_encryption_enabled is not None:
        out["at_rest_encryption_enabled"] = (
            child_at_rest_encryption_enabled.text or ""
        ).lower() == "true"
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    return out
