"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RdsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.double_optional
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.string


class RdsConfiguration(TypedDict):
    engine_edition: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>Describes the recommended target Amazon RDS engine edition.</p>"""
    instance_type: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>Describes the recommended target Amazon RDS instance type.</p>"""
    instance_vcpu: NotRequired[
        "aws_sdk_database_migration_service.types.double_optional.DoubleOptional"
    ]
    """<p>Describes the number of virtual CPUs (vCPU) on the recommended Amazon RDS DB instance that meets your requirements.</p>"""
    instance_memory: NotRequired[
        "aws_sdk_database_migration_service.types.double_optional.DoubleOptional"
    ]
    """<p>Describes the memory on the recommended Amazon RDS DB instance that meets your requirements.</p>"""
    storage_type: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>Describes the storage type of the recommended Amazon RDS DB instance that meets your requirements.</p> <p>Amazon RDS provides three storage types: General Purpose SSD (also known as gp2 and gp3), Provisioned IOPS SSD (also known as io1), and magnetic (also known as standard).</p>"""
    storage_size: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Describes the storage size of the recommended Amazon RDS DB instance that meets your requirements.</p>"""
    storage_iops: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Describes the number of I/O operations completed each second (IOPS) on the recommended Amazon RDS DB instance that meets your requirements.</p>"""
    deployment_option: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>Describes the deployment option for the recommended Amazon RDS DB instance. The deployment options include Multi-AZ and Single-AZ deployments. Valid values include <code>\"MULTI_AZ\"</code> and <code>\"SINGLE_AZ\"</code>.</p>"""
    engine_version: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>Describes the recommended target Amazon RDS engine version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RdsConfiguration) -> dict:
    out: dict = {}
    if "engine_edition" in value:
        out["EngineEdition"] = value["engine_edition"]
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "instance_vcpu" in value:
        out["InstanceVcpu"] = value["instance_vcpu"]
    if "instance_memory" in value:
        out["InstanceMemory"] = value["instance_memory"]
    if "storage_type" in value:
        out["StorageType"] = value["storage_type"]
    if "storage_size" in value:
        out["StorageSize"] = value["storage_size"]
    if "storage_iops" in value:
        out["StorageIops"] = value["storage_iops"]
    if "deployment_option" in value:
        out["DeploymentOption"] = value["deployment_option"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RdsConfiguration:
    out: RdsConfiguration = {}  # type: ignore[typeddict-item]
    if "EngineEdition" in data:
        out["engine_edition"] = data["EngineEdition"]
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "InstanceVcpu" in data:
        out["instance_vcpu"] = data["InstanceVcpu"]
    if "InstanceMemory" in data:
        out["instance_memory"] = data["InstanceMemory"]
    if "StorageType" in data:
        out["storage_type"] = data["StorageType"]
    if "StorageSize" in data:
        out["storage_size"] = data["StorageSize"]
    if "StorageIops" in data:
        out["storage_iops"] = data["StorageIops"]
    if "DeploymentOption" in data:
        out["deployment_option"] = data["DeploymentOption"]
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    return out
