"""Generated from Smithy shape ``com.amazonaws.neptune#OrderableDBInstanceOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.availability_zone_list
    import capo_neptune.types.boolean
    import capo_neptune.types.double_optional
    import capo_neptune.types.integer_optional
    import capo_neptune.types.string
    import capo_neptune.types.string_list


class OrderableDBInstanceOption(TypedDict, closed=True):
    engine: NotRequired["capo_neptune.types.string.String"]
    """<p>The engine type of a DB instance.</p>"""
    engine_version: NotRequired["capo_neptune.types.string.String"]
    """<p>The engine version of a DB instance.</p>"""
    db_instance_class: NotRequired["capo_neptune.types.string.String"]
    """<p>The DB instance class for a DB instance.</p>"""
    license_model: NotRequired["capo_neptune.types.string.String"]
    """<p>The license model for a DB instance.</p>"""
    availability_zones: NotRequired[
        "capo_neptune.types.availability_zone_list.AvailabilityZoneList"
    ]
    """<p>A list of Availability Zones for a DB instance.</p>"""
    multi_az_capable: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>Indicates whether a DB instance is Multi-AZ capable.</p>"""
    read_replica_capable: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>Indicates whether a DB instance can have a Read Replica.</p>"""
    vpc: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>Indicates whether a DB instance is in a VPC.</p>"""
    supports_storage_encryption: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>Indicates whether a DB instance supports encrypted storage.</p>"""
    storage_type: NotRequired["capo_neptune.types.string.String"]
    """<p>Not applicable. In Neptune the storage type is managed at the DB Cluster level.</p>"""
    supports_iops: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>Indicates whether a DB instance supports provisioned IOPS.</p>"""
    supports_enhanced_monitoring: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>Indicates whether a DB instance supports Enhanced Monitoring at intervals from 1 to 60 seconds.</p>"""
    supports_iam_database_authentication: NotRequired[
        "capo_neptune.types.boolean.Boolean"
    ]
    """<p>Indicates whether a DB instance supports IAM database authentication.</p>"""
    supports_performance_insights: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p> <i>(Not supported by Neptune)</i> </p>"""
    min_storage_size: NotRequired["capo_neptune.types.integer_optional.IntegerOptional"]
    """<p>Minimum storage size for a DB instance.</p>"""
    max_storage_size: NotRequired["capo_neptune.types.integer_optional.IntegerOptional"]
    """<p>Maximum storage size for a DB instance.</p>"""
    min_iops_per_db_instance: NotRequired[
        "capo_neptune.types.integer_optional.IntegerOptional"
    ]
    """<p>Minimum total provisioned IOPS for a DB instance.</p>"""
    max_iops_per_db_instance: NotRequired[
        "capo_neptune.types.integer_optional.IntegerOptional"
    ]
    """<p>Maximum total provisioned IOPS for a DB instance.</p>"""
    min_iops_per_gib: NotRequired["capo_neptune.types.double_optional.DoubleOptional"]
    """<p>Minimum provisioned IOPS per GiB for a DB instance.</p>"""
    max_iops_per_gib: NotRequired["capo_neptune.types.double_optional.DoubleOptional"]
    """<p>Maximum provisioned IOPS per GiB for a DB instance.</p>"""
    supports_global_databases: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p>A value that indicates whether you can use Neptune global databases with a specific combination of other DB engine attributes.</p>"""
    supported_network_types: NotRequired["capo_neptune.types.string_list.StringList"]
    """<p>The network types supported by the orderable DB instance option.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OrderableDBInstanceOption, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "engine" in value:
        pairs.append((f"{key_prefix}Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{key_prefix}EngineVersion", str(value["engine_version"])))
    if "db_instance_class" in value:
        pairs.append((f"{key_prefix}DBInstanceClass", str(value["db_instance_class"])))
    if "license_model" in value:
        pairs.append((f"{key_prefix}LicenseModel", str(value["license_model"])))
    if "availability_zones" in value:
        import capo_neptune.types.availability_zone_list

        capo_neptune.types.availability_zone_list.serialize_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZones"
        )
    if "multi_az_capable" in value:
        pairs.append(
            (
                f"{key_prefix}MultiAZCapable",
                "true" if value["multi_az_capable"] else "false",
            )
        )
    if "read_replica_capable" in value:
        pairs.append(
            (
                f"{key_prefix}ReadReplicaCapable",
                "true" if value["read_replica_capable"] else "false",
            )
        )
    if "vpc" in value:
        pairs.append((f"{key_prefix}Vpc", "true" if value["vpc"] else "false"))
    if "supports_storage_encryption" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsStorageEncryption",
                "true" if value["supports_storage_encryption"] else "false",
            )
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "supports_iops" in value:
        pairs.append(
            (f"{key_prefix}SupportsIops", "true" if value["supports_iops"] else "false")
        )
    if "supports_enhanced_monitoring" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsEnhancedMonitoring",
                "true" if value["supports_enhanced_monitoring"] else "false",
            )
        )
    if "supports_iam_database_authentication" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsIAMDatabaseAuthentication",
                "true" if value["supports_iam_database_authentication"] else "false",
            )
        )
    if "supports_performance_insights" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsPerformanceInsights",
                "true" if value["supports_performance_insights"] else "false",
            )
        )
    if "min_storage_size" in value:
        pairs.append((f"{key_prefix}MinStorageSize", str(value["min_storage_size"])))
    if "max_storage_size" in value:
        pairs.append((f"{key_prefix}MaxStorageSize", str(value["max_storage_size"])))
    if "min_iops_per_db_instance" in value:
        pairs.append(
            (
                f"{key_prefix}MinIopsPerDbInstance",
                str(value["min_iops_per_db_instance"]),
            )
        )
    if "max_iops_per_db_instance" in value:
        pairs.append(
            (
                f"{key_prefix}MaxIopsPerDbInstance",
                str(value["max_iops_per_db_instance"]),
            )
        )
    if "min_iops_per_gib" in value:
        pairs.append((f"{key_prefix}MinIopsPerGib", str(value["min_iops_per_gib"])))
    if "max_iops_per_gib" in value:
        pairs.append((f"{key_prefix}MaxIopsPerGib", str(value["max_iops_per_gib"])))
    if "supports_global_databases" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsGlobalDatabases",
                "true" if value["supports_global_databases"] else "false",
            )
        )
    if "supported_network_types" in value:
        import capo_neptune.types.string_list

        capo_neptune.types.string_list.serialize_query(
            value["supported_network_types"],
            pairs,
            f"{key_prefix}SupportedNetworkTypes",
        )


def deserialize_query(el: Element) -> OrderableDBInstanceOption:
    out: OrderableDBInstanceOption = {}  # type: ignore[typeddict-item]
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
    child_license_model = el.find("LicenseModel")
    if child_license_model is not None:
        out["license_model"] = str(child_license_model.text or "")
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import capo_neptune.types.availability_zone_list

        out["availability_zones"] = (
            capo_neptune.types.availability_zone_list.deserialize_query(
                child_availability_zones
            )
        )
    child_multi_az_capable = el.find("MultiAZCapable")
    if child_multi_az_capable is not None:
        out["multi_az_capable"] = (child_multi_az_capable.text or "").lower() == "true"
    child_read_replica_capable = el.find("ReadReplicaCapable")
    if child_read_replica_capable is not None:
        out["read_replica_capable"] = (
            child_read_replica_capable.text or ""
        ).lower() == "true"
    child_vpc = el.find("Vpc")
    if child_vpc is not None:
        out["vpc"] = (child_vpc.text or "").lower() == "true"
    child_supports_storage_encryption = el.find("SupportsStorageEncryption")
    if child_supports_storage_encryption is not None:
        out["supports_storage_encryption"] = (
            child_supports_storage_encryption.text or ""
        ).lower() == "true"
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_supports_iops = el.find("SupportsIops")
    if child_supports_iops is not None:
        out["supports_iops"] = (child_supports_iops.text or "").lower() == "true"
    child_supports_enhanced_monitoring = el.find("SupportsEnhancedMonitoring")
    if child_supports_enhanced_monitoring is not None:
        out["supports_enhanced_monitoring"] = (
            child_supports_enhanced_monitoring.text or ""
        ).lower() == "true"
    child_supports_iam_database_authentication = el.find(
        "SupportsIAMDatabaseAuthentication"
    )
    if child_supports_iam_database_authentication is not None:
        out["supports_iam_database_authentication"] = (
            child_supports_iam_database_authentication.text or ""
        ).lower() == "true"
    child_supports_performance_insights = el.find("SupportsPerformanceInsights")
    if child_supports_performance_insights is not None:
        out["supports_performance_insights"] = (
            child_supports_performance_insights.text or ""
        ).lower() == "true"
    child_min_storage_size = el.find("MinStorageSize")
    if child_min_storage_size is not None:
        out["min_storage_size"] = int(child_min_storage_size.text or "")
    child_max_storage_size = el.find("MaxStorageSize")
    if child_max_storage_size is not None:
        out["max_storage_size"] = int(child_max_storage_size.text or "")
    child_min_iops_per_db_instance = el.find("MinIopsPerDbInstance")
    if child_min_iops_per_db_instance is not None:
        out["min_iops_per_db_instance"] = int(child_min_iops_per_db_instance.text or "")
    child_max_iops_per_db_instance = el.find("MaxIopsPerDbInstance")
    if child_max_iops_per_db_instance is not None:
        out["max_iops_per_db_instance"] = int(child_max_iops_per_db_instance.text or "")
    child_min_iops_per_gib = el.find("MinIopsPerGib")
    if child_min_iops_per_gib is not None:
        out["min_iops_per_gib"] = float(child_min_iops_per_gib.text or "")
    child_max_iops_per_gib = el.find("MaxIopsPerGib")
    if child_max_iops_per_gib is not None:
        out["max_iops_per_gib"] = float(child_max_iops_per_gib.text or "")
    child_supports_global_databases = el.find("SupportsGlobalDatabases")
    if child_supports_global_databases is not None:
        out["supports_global_databases"] = (
            child_supports_global_databases.text or ""
        ).lower() == "true"
    child_supported_network_types = el.find("SupportedNetworkTypes")
    if child_supported_network_types is not None:
        import capo_neptune.types.string_list

        out["supported_network_types"] = (
            capo_neptune.types.string_list.deserialize_query(
                child_supported_network_types
            )
        )
    return out
