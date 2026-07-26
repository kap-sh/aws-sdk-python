"""Generated from Smithy shape ``com.amazonaws.elasticache#ReplicationGroupPendingModifiedValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.auth_token_update_status
    import capo_elasticache.types.boolean_optional
    import capo_elasticache.types.cluster_mode
    import capo_elasticache.types.pending_automatic_failover_status
    import capo_elasticache.types.pending_log_delivery_configuration_list
    import capo_elasticache.types.resharding_status
    import capo_elasticache.types.string
    import capo_elasticache.types.transit_encryption_mode
    import capo_elasticache.types.user_groups_update_status


class ReplicationGroupPendingModifiedValues(TypedDict, closed=True):
    primary_cluster_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The primary cluster ID that is applied immediately (if <code>--apply-immediately</code> was specified), or during the next maintenance window.</p>"""
    automatic_failover_status: NotRequired[
        "capo_elasticache.types.pending_automatic_failover_status.PendingAutomaticFailoverStatus"
    ]
    """<p>Indicates the status of automatic failover for this Valkey or Redis OSS replication group.</p>"""
    resharding: NotRequired["capo_elasticache.types.resharding_status.ReshardingStatus"]
    """<p>The status of an online resharding operation.</p>"""
    auth_token_status: NotRequired[
        "capo_elasticache.types.auth_token_update_status.AuthTokenUpdateStatus"
    ]
    """<p>The auth token status</p>"""
    user_groups: NotRequired[
        "capo_elasticache.types.user_groups_update_status.UserGroupsUpdateStatus"
    ]
    """<p>The user group being modified.</p>"""
    log_delivery_configurations: NotRequired[
        "capo_elasticache.types.pending_log_delivery_configuration_list.PendingLogDeliveryConfigurationList"
    ]
    """<p>The log delivery configurations being modified </p>"""
    transit_encryption_enabled: NotRequired[
        "capo_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>A flag that enables in-transit encryption when set to true.</p>"""
    transit_encryption_mode: NotRequired[
        "capo_elasticache.types.transit_encryption_mode.TransitEncryptionMode"
    ]
    """<p>A setting that allows you to migrate your clients to use in-transit encryption, with no downtime.</p>"""
    cluster_mode: NotRequired["capo_elasticache.types.cluster_mode.ClusterMode"]
    """<p>Enabled or Disabled. To modify cluster mode from Disabled to Enabled, you must first set the cluster mode to Compatible. Compatible mode allows your Valkey or Redis OSS clients to connect using both cluster mode enabled and cluster mode disabled. After you migrate all Valkey or Redis OSS clients to use cluster mode enabled, you can then complete cluster mode configuration and set the cluster mode to Enabled.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReplicationGroupPendingModifiedValues,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "primary_cluster_id" in value:
        pairs.append((f"{prefix}.PrimaryClusterId", str(value["primary_cluster_id"])))
    if "automatic_failover_status" in value:
        import capo_elasticache.types.pending_automatic_failover_status

        capo_elasticache.types.pending_automatic_failover_status.serialize_query(
            value["automatic_failover_status"],
            pairs,
            f"{prefix}.AutomaticFailoverStatus",
        )
    if "resharding" in value:
        import capo_elasticache.types.resharding_status

        capo_elasticache.types.resharding_status.serialize_query(
            value["resharding"], pairs, f"{prefix}.Resharding"
        )
    if "auth_token_status" in value:
        import capo_elasticache.types.auth_token_update_status

        capo_elasticache.types.auth_token_update_status.serialize_query(
            value["auth_token_status"], pairs, f"{prefix}.AuthTokenStatus"
        )
    if "user_groups" in value:
        import capo_elasticache.types.user_groups_update_status

        capo_elasticache.types.user_groups_update_status.serialize_query(
            value["user_groups"], pairs, f"{prefix}.UserGroups"
        )
    if "log_delivery_configurations" in value:
        import capo_elasticache.types.pending_log_delivery_configuration_list

        capo_elasticache.types.pending_log_delivery_configuration_list.serialize_query(
            value["log_delivery_configurations"],
            pairs,
            f"{prefix}.LogDeliveryConfigurations",
        )
    if "transit_encryption_enabled" in value:
        pairs.append(
            (
                f"{prefix}.TransitEncryptionEnabled",
                "true" if value["transit_encryption_enabled"] else "false",
            )
        )
    if "transit_encryption_mode" in value:
        import capo_elasticache.types.transit_encryption_mode

        capo_elasticache.types.transit_encryption_mode.serialize_query(
            value["transit_encryption_mode"], pairs, f"{prefix}.TransitEncryptionMode"
        )
    if "cluster_mode" in value:
        import capo_elasticache.types.cluster_mode

        capo_elasticache.types.cluster_mode.serialize_query(
            value["cluster_mode"], pairs, f"{prefix}.ClusterMode"
        )


def deserialize_query(el: Element) -> ReplicationGroupPendingModifiedValues:
    out: ReplicationGroupPendingModifiedValues = {}  # type: ignore[typeddict-item]
    child_primary_cluster_id = el.find("PrimaryClusterId")
    if child_primary_cluster_id is not None:
        out["primary_cluster_id"] = str(child_primary_cluster_id.text or "")
    child_automatic_failover_status = el.find("AutomaticFailoverStatus")
    if child_automatic_failover_status is not None:
        import capo_elasticache.types.pending_automatic_failover_status

        out["automatic_failover_status"] = (
            capo_elasticache.types.pending_automatic_failover_status.deserialize_query(
                child_automatic_failover_status
            )
        )
    child_resharding = el.find("Resharding")
    if child_resharding is not None:
        import capo_elasticache.types.resharding_status

        out["resharding"] = capo_elasticache.types.resharding_status.deserialize_query(
            child_resharding
        )
    child_auth_token_status = el.find("AuthTokenStatus")
    if child_auth_token_status is not None:
        import capo_elasticache.types.auth_token_update_status

        out["auth_token_status"] = (
            capo_elasticache.types.auth_token_update_status.deserialize_query(
                child_auth_token_status
            )
        )
    child_user_groups = el.find("UserGroups")
    if child_user_groups is not None:
        import capo_elasticache.types.user_groups_update_status

        out["user_groups"] = (
            capo_elasticache.types.user_groups_update_status.deserialize_query(
                child_user_groups
            )
        )
    child_log_delivery_configurations = el.find("LogDeliveryConfigurations")
    if child_log_delivery_configurations is not None:
        import capo_elasticache.types.pending_log_delivery_configuration_list

        out["log_delivery_configurations"] = (
            capo_elasticache.types.pending_log_delivery_configuration_list.deserialize_query(
                child_log_delivery_configurations
            )
        )
    child_transit_encryption_enabled = el.find("TransitEncryptionEnabled")
    if child_transit_encryption_enabled is not None:
        out["transit_encryption_enabled"] = (
            child_transit_encryption_enabled.text or ""
        ).lower() == "true"
    child_transit_encryption_mode = el.find("TransitEncryptionMode")
    if child_transit_encryption_mode is not None:
        import capo_elasticache.types.transit_encryption_mode

        out["transit_encryption_mode"] = (
            capo_elasticache.types.transit_encryption_mode.deserialize_query(
                child_transit_encryption_mode
            )
        )
    child_cluster_mode = el.find("ClusterMode")
    if child_cluster_mode is not None:
        import capo_elasticache.types.cluster_mode

        out["cluster_mode"] = capo_elasticache.types.cluster_mode.deserialize_query(
            child_cluster_mode
        )
    return out
