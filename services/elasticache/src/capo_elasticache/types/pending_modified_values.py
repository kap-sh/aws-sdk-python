"""Generated from Smithy shape ``com.amazonaws.elasticache#PendingModifiedValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.auth_token_update_status
    import capo_elasticache.types.boolean_optional
    import capo_elasticache.types.cache_node_ids_list
    import capo_elasticache.types.integer_optional
    import capo_elasticache.types.pending_log_delivery_configuration_list
    import capo_elasticache.types.scale_config
    import capo_elasticache.types.string
    import capo_elasticache.types.transit_encryption_mode


class PendingModifiedValues(TypedDict, closed=True):
    num_cache_nodes: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The new number of cache nodes for the cluster.</p> <p>For clusters running Valkey or Redis OSS, this value must be 1. For clusters running Memcached, this value must be between 1 and 40.</p>"""
    cache_node_ids_to_remove: NotRequired[
        "capo_elasticache.types.cache_node_ids_list.CacheNodeIdsList"
    ]
    """<p>A list of cache node IDs that are being removed (or will be removed) from the cluster. A node ID is a 4-digit numeric identifier (0001, 0002, etc.).</p>"""
    engine_version: NotRequired["capo_elasticache.types.string.String"]
    """<p>The new cache engine version that the cluster runs.</p>"""
    cache_node_type: NotRequired["capo_elasticache.types.string.String"]
    """<p>The cache node type that this cluster or replication group is scaled to.</p>"""
    auth_token_status: NotRequired[
        "capo_elasticache.types.auth_token_update_status.AuthTokenUpdateStatus"
    ]
    """<p>The auth token status</p>"""
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
    scale_config: NotRequired["capo_elasticache.types.scale_config.ScaleConfig"]
    """<p>The scaling configuration changes that are pending for the Memcached cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PendingModifiedValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "num_cache_nodes" in value:
        pairs.append((f"{prefix}.NumCacheNodes", str(value["num_cache_nodes"])))
    if "cache_node_ids_to_remove" in value:
        import capo_elasticache.types.cache_node_ids_list

        capo_elasticache.types.cache_node_ids_list.serialize_query(
            value["cache_node_ids_to_remove"], pairs, f"{prefix}.CacheNodeIdsToRemove"
        )
    if "engine_version" in value:
        pairs.append((f"{prefix}.EngineVersion", str(value["engine_version"])))
    if "cache_node_type" in value:
        pairs.append((f"{prefix}.CacheNodeType", str(value["cache_node_type"])))
    if "auth_token_status" in value:
        import capo_elasticache.types.auth_token_update_status

        capo_elasticache.types.auth_token_update_status.serialize_query(
            value["auth_token_status"], pairs, f"{prefix}.AuthTokenStatus"
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
    if "scale_config" in value:
        import capo_elasticache.types.scale_config

        capo_elasticache.types.scale_config.serialize_query(
            value["scale_config"], pairs, f"{prefix}.ScaleConfig"
        )


def deserialize_query(el: Element) -> PendingModifiedValues:
    out: PendingModifiedValues = {}  # type: ignore[typeddict-item]
    child_num_cache_nodes = el.find("NumCacheNodes")
    if child_num_cache_nodes is not None:
        out["num_cache_nodes"] = int(child_num_cache_nodes.text or "")
    child_cache_node_ids_to_remove = el.find("CacheNodeIdsToRemove")
    if child_cache_node_ids_to_remove is not None:
        import capo_elasticache.types.cache_node_ids_list

        out["cache_node_ids_to_remove"] = (
            capo_elasticache.types.cache_node_ids_list.deserialize_query(
                child_cache_node_ids_to_remove
            )
        )
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_cache_node_type = el.find("CacheNodeType")
    if child_cache_node_type is not None:
        out["cache_node_type"] = str(child_cache_node_type.text or "")
    child_auth_token_status = el.find("AuthTokenStatus")
    if child_auth_token_status is not None:
        import capo_elasticache.types.auth_token_update_status

        out["auth_token_status"] = (
            capo_elasticache.types.auth_token_update_status.deserialize_query(
                child_auth_token_status
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
    child_scale_config = el.find("ScaleConfig")
    if child_scale_config is not None:
        import capo_elasticache.types.scale_config

        out["scale_config"] = capo_elasticache.types.scale_config.deserialize_query(
            child_scale_config
        )
    return out
