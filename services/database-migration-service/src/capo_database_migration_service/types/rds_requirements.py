"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RdsRequirements``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.double_optional
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.string


class RdsRequirements(TypedDict, closed=True):
    engine_edition: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The required target Amazon RDS engine edition.</p>"""
    instance_vcpu: NotRequired[
        "capo_database_migration_service.types.double_optional.DoubleOptional"
    ]
    """<p>The required number of virtual CPUs (vCPU) on the Amazon RDS DB instance.</p>"""
    instance_memory: NotRequired[
        "capo_database_migration_service.types.double_optional.DoubleOptional"
    ]
    """<p>The required memory on the Amazon RDS DB instance.</p>"""
    storage_size: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The required Amazon RDS DB instance storage size.</p>"""
    storage_iops: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The required number of I/O operations completed each second (IOPS) on your Amazon RDS DB instance.</p>"""
    deployment_option: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    r"""<p>The required deployment option for the Amazon RDS DB instance. Valid values include <code>\"MULTI_AZ\"</code> for Multi-AZ deployments and <code>\"SINGLE_AZ\"</code> for Single-AZ deployments.</p>"""
    engine_version: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The required target Amazon RDS engine version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RdsRequirements) -> dict:
    out: dict = {}
    if "engine_edition" in value:
        out["EngineEdition"] = value["engine_edition"]
    if "instance_vcpu" in value:
        out["InstanceVcpu"] = value["instance_vcpu"]
    if "instance_memory" in value:
        out["InstanceMemory"] = value["instance_memory"]
    if "storage_size" in value:
        out["StorageSize"] = value["storage_size"]
    if "storage_iops" in value:
        out["StorageIops"] = value["storage_iops"]
    if "deployment_option" in value:
        out["DeploymentOption"] = value["deployment_option"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RdsRequirements:
    out: RdsRequirements = {}  # type: ignore[typeddict-item]
    if "EngineEdition" in data:
        out["engine_edition"] = data["EngineEdition"]
    if "InstanceVcpu" in data:
        out["instance_vcpu"] = data["InstanceVcpu"]
    if "InstanceMemory" in data:
        out["instance_memory"] = data["InstanceMemory"]
    if "StorageSize" in data:
        out["storage_size"] = data["StorageSize"]
    if "StorageIops" in data:
        out["storage_iops"] = data["StorageIops"]
    if "DeploymentOption" in data:
        out["deployment_option"] = data["DeploymentOption"]
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    return out
