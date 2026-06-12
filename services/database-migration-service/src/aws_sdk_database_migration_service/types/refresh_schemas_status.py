"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RefreshSchemasStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.refresh_schemas_status_type_value
    import aws_sdk_database_migration_service.types.string
    import aws_sdk_database_migration_service.types.t_stamp


class RefreshSchemasStatus(TypedDict):
    endpoint_arn: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.</p>"""
    replication_instance_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the replication instance.</p>"""
    status: NotRequired[
        "aws_sdk_database_migration_service.types.refresh_schemas_status_type_value.RefreshSchemasStatusTypeValue"
    ]
    """<p>The status of the schema.</p>"""
    last_refresh_date: NotRequired[
        "aws_sdk_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The date the schema was last refreshed.</p>"""
    last_failure_message: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The last failure message for the schema.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RefreshSchemasStatus) -> dict:
    out: dict = {}
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    if "replication_instance_arn" in value:
        out["ReplicationInstanceArn"] = value["replication_instance_arn"]
    if "status" in value:
        import aws_sdk_database_migration_service.types.refresh_schemas_status_type_value

        out["Status"] = (
            aws_sdk_database_migration_service.types.refresh_schemas_status_type_value.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "last_refresh_date" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["LastRefreshDate"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["last_refresh_date"]
            )
        )
    if "last_failure_message" in value:
        out["LastFailureMessage"] = value["last_failure_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RefreshSchemasStatus:
    out: RefreshSchemasStatus = {}  # type: ignore[typeddict-item]
    if "EndpointArn" in data:
        out["endpoint_arn"] = data["EndpointArn"]
    if "ReplicationInstanceArn" in data:
        out["replication_instance_arn"] = data["ReplicationInstanceArn"]
    if "Status" in data:
        import aws_sdk_database_migration_service.types.refresh_schemas_status_type_value

        out["status"] = (
            aws_sdk_database_migration_service.types.refresh_schemas_status_type_value.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "LastRefreshDate" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["last_refresh_date"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["LastRefreshDate"]
            )
        )
    if "LastFailureMessage" in data:
        out["last_failure_message"] = data["LastFailureMessage"]
    return out
