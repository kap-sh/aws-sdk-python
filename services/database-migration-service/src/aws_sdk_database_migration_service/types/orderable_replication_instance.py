"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#OrderableReplicationInstance``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.availability_zones_list
    import aws_sdk_database_migration_service.types.integer
    import aws_sdk_database_migration_service.types.release_status_values
    import aws_sdk_database_migration_service.types.replication_instance_class
    import aws_sdk_database_migration_service.types.string


class OrderableReplicationInstance(TypedDict):
    engine_version: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The version of the replication engine.</p>"""
    replication_instance_class: NotRequired[
        "aws_sdk_database_migration_service.types.replication_instance_class.ReplicationInstanceClass"
    ]
    r"""<p>The compute and memory capacity of the replication instance as defined for the specified replication instance class. For example to specify the instance class dms.c4.large, set this parameter to <code>\"dms.c4.large\"</code>.</p> <p>For more information on the settings and capacities for the available replication instance classes, see <a href=\"https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.InDepth\"> Selecting the right DMS replication instance for your migration</a>. </p>"""
    storage_type: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The type of storage used by the replication instance.</p>"""
    min_allocated_storage: "aws_sdk_database_migration_service.types.integer.Integer"
    """<p>The minimum amount of storage (in gigabytes) that can be allocated for the replication instance.</p>"""
    max_allocated_storage: "aws_sdk_database_migration_service.types.integer.Integer"
    """<p>The minimum amount of storage (in gigabytes) that can be allocated for the replication instance.</p>"""
    default_allocated_storage: (
        "aws_sdk_database_migration_service.types.integer.Integer"
    )
    """<p>The default amount of storage (in gigabytes) that is allocated for the replication instance.</p>"""
    included_allocated_storage: (
        "aws_sdk_database_migration_service.types.integer.Integer"
    )
    """<p>The amount of storage (in gigabytes) that is allocated for the replication instance.</p>"""
    availability_zones: NotRequired[
        "aws_sdk_database_migration_service.types.availability_zones_list.AvailabilityZonesList"
    ]
    """<p>List of Availability Zones for this replication instance.</p>"""
    release_status: NotRequired[
        "aws_sdk_database_migration_service.types.release_status_values.ReleaseStatusValues"
    ]
    """<p>The value returned when the specified <code>EngineVersion</code> of the replication instance is in Beta or test mode. This indicates some features might not work as expected.</p> <note> <p>DMS supports the <code>ReleaseStatus</code> parameter in versions 3.1.4 and later.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrderableReplicationInstance) -> dict:
    out: dict = {}
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "replication_instance_class" in value:
        out["ReplicationInstanceClass"] = value["replication_instance_class"]
    if "storage_type" in value:
        out["StorageType"] = value["storage_type"]
    out["MinAllocatedStorage"] = value.get("min_allocated_storage", 0)
    out["MaxAllocatedStorage"] = value.get("max_allocated_storage", 0)
    out["DefaultAllocatedStorage"] = value.get("default_allocated_storage", 0)
    out["IncludedAllocatedStorage"] = value.get("included_allocated_storage", 0)
    if "availability_zones" in value:
        import aws_sdk_database_migration_service.types.availability_zones_list

        out["AvailabilityZones"] = (
            aws_sdk_database_migration_service.types.availability_zones_list.serialize_aws_json_1_1(
                value["availability_zones"]
            )
        )
    if "release_status" in value:
        import aws_sdk_database_migration_service.types.release_status_values

        out["ReleaseStatus"] = (
            aws_sdk_database_migration_service.types.release_status_values.serialize_aws_json_1_1(
                value["release_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OrderableReplicationInstance:
    out: OrderableReplicationInstance = {}  # type: ignore[typeddict-item]
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "ReplicationInstanceClass" in data:
        out["replication_instance_class"] = data["ReplicationInstanceClass"]
    if "StorageType" in data:
        out["storage_type"] = data["StorageType"]
    if "MinAllocatedStorage" in data:
        out["min_allocated_storage"] = data["MinAllocatedStorage"]
    else:
        out["min_allocated_storage"] = 0
    if "MaxAllocatedStorage" in data:
        out["max_allocated_storage"] = data["MaxAllocatedStorage"]
    else:
        out["max_allocated_storage"] = 0
    if "DefaultAllocatedStorage" in data:
        out["default_allocated_storage"] = data["DefaultAllocatedStorage"]
    else:
        out["default_allocated_storage"] = 0
    if "IncludedAllocatedStorage" in data:
        out["included_allocated_storage"] = data["IncludedAllocatedStorage"]
    else:
        out["included_allocated_storage"] = 0
    if "AvailabilityZones" in data:
        import aws_sdk_database_migration_service.types.availability_zones_list

        out["availability_zones"] = (
            aws_sdk_database_migration_service.types.availability_zones_list.deserialize_aws_json_1_1(
                data["AvailabilityZones"]
            )
        )
    if "ReleaseStatus" in data:
        import aws_sdk_database_migration_service.types.release_status_values

        out["release_status"] = (
            aws_sdk_database_migration_service.types.release_status_values.deserialize_aws_json_1_1(
                data["ReleaseStatus"]
            )
        )
    return out
