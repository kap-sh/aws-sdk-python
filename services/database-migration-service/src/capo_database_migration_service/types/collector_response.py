"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CollectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.collector_health_check
    import capo_database_migration_service.types.inventory_data
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.version_status


class CollectorResponse(TypedDict, closed=True):
    collector_referenced_id: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The reference ID of the Fleet Advisor collector.</p>"""
    collector_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name of the Fleet Advisor collector .</p>"""
    collector_version: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The version of your Fleet Advisor collector, in semantic versioning format, for example <code>1.0.2</code> </p>"""
    version_status: NotRequired[
        "capo_database_migration_service.types.version_status.VersionStatus"
    ]
    """<p>Whether the collector version is up to date.</p>"""
    description: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>A summary description of the Fleet Advisor collector.</p>"""
    s3_bucket_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The Amazon S3 bucket that the Fleet Advisor collector uses to store inventory metadata.</p>"""
    service_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The IAM role that grants permissions to access the specified Amazon S3 bucket.</p>"""
    collector_health_check: NotRequired[
        "capo_database_migration_service.types.collector_health_check.CollectorHealthCheck"
    ]
    last_data_received: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The timestamp of the last time the collector received data, in the following format: <code>2022-01-24T19:04:02.596113Z</code> </p>"""
    registered_date: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The timestamp when DMS registered the collector, in the following format: <code>2022-01-24T19:04:02.596113Z</code> </p>"""
    created_date: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The timestamp when you created the collector, in the following format: <code>2022-01-24T19:04:02.596113Z</code> </p>"""
    modified_date: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The timestamp when DMS last modified the collector, in the following format: <code>2022-01-24T19:04:02.596113Z</code> </p>"""
    inventory_data: NotRequired[
        "capo_database_migration_service.types.inventory_data.InventoryData"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CollectorResponse) -> dict:
    out: dict = {}
    if "collector_referenced_id" in value:
        out["CollectorReferencedId"] = value["collector_referenced_id"]
    if "collector_name" in value:
        out["CollectorName"] = value["collector_name"]
    if "collector_version" in value:
        out["CollectorVersion"] = value["collector_version"]
    if "version_status" in value:
        import capo_database_migration_service.types.version_status

        out["VersionStatus"] = (
            capo_database_migration_service.types.version_status.serialize_aws_json_1_1(
                value["version_status"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    if "service_access_role_arn" in value:
        out["ServiceAccessRoleArn"] = value["service_access_role_arn"]
    if "collector_health_check" in value:
        import capo_database_migration_service.types.collector_health_check

        out["CollectorHealthCheck"] = (
            capo_database_migration_service.types.collector_health_check.serialize_aws_json_1_1(
                value["collector_health_check"]
            )
        )
    if "last_data_received" in value:
        out["LastDataReceived"] = value["last_data_received"]
    if "registered_date" in value:
        out["RegisteredDate"] = value["registered_date"]
    if "created_date" in value:
        out["CreatedDate"] = value["created_date"]
    if "modified_date" in value:
        out["ModifiedDate"] = value["modified_date"]
    if "inventory_data" in value:
        import capo_database_migration_service.types.inventory_data

        out["InventoryData"] = (
            capo_database_migration_service.types.inventory_data.serialize_aws_json_1_1(
                value["inventory_data"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CollectorResponse:
    out: CollectorResponse = {}  # type: ignore[typeddict-item]
    if "CollectorReferencedId" in data:
        out["collector_referenced_id"] = data["CollectorReferencedId"]
    if "CollectorName" in data:
        out["collector_name"] = data["CollectorName"]
    if "CollectorVersion" in data:
        out["collector_version"] = data["CollectorVersion"]
    if "VersionStatus" in data:
        import capo_database_migration_service.types.version_status

        out["version_status"] = (
            capo_database_migration_service.types.version_status.deserialize_aws_json_1_1(
                data["VersionStatus"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    if "ServiceAccessRoleArn" in data:
        out["service_access_role_arn"] = data["ServiceAccessRoleArn"]
    if "CollectorHealthCheck" in data:
        import capo_database_migration_service.types.collector_health_check

        out["collector_health_check"] = (
            capo_database_migration_service.types.collector_health_check.deserialize_aws_json_1_1(
                data["CollectorHealthCheck"]
            )
        )
    if "LastDataReceived" in data:
        out["last_data_received"] = data["LastDataReceived"]
    if "RegisteredDate" in data:
        out["registered_date"] = data["RegisteredDate"]
    if "CreatedDate" in data:
        out["created_date"] = data["CreatedDate"]
    if "ModifiedDate" in data:
        out["modified_date"] = data["ModifiedDate"]
    if "InventoryData" in data:
        import capo_database_migration_service.types.inventory_data

        out["inventory_data"] = (
            capo_database_migration_service.types.inventory_data.deserialize_aws_json_1_1(
                data["InventoryData"]
            )
        )
    return out
