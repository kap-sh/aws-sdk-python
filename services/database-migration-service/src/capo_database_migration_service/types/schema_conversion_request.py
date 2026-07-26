"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SchemaConversionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.error_details
    import capo_database_migration_service.types.export_sql_details
    import capo_database_migration_service.types.progress
    import capo_database_migration_service.types.string


class SchemaConversionRequest(TypedDict, closed=True):
    status: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The schema conversion action status.</p>"""
    request_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The identifier for the schema conversion action.</p>"""
    migration_project_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The migration project ARN.</p>"""
    error: NotRequired[
        "capo_database_migration_service.types.error_details.ErrorDetails"
    ]
    export_sql_details: NotRequired[
        "capo_database_migration_service.types.export_sql_details.ExportSqlDetails"
    ]
    progress: NotRequired["capo_database_migration_service.types.progress.Progress"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaConversionRequest) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    if "request_identifier" in value:
        out["RequestIdentifier"] = value["request_identifier"]
    if "migration_project_arn" in value:
        out["MigrationProjectArn"] = value["migration_project_arn"]
    if "error" in value:
        import capo_database_migration_service.types.error_details

        out["Error"] = (
            capo_database_migration_service.types.error_details.serialize_aws_json_1_1(
                value["error"]
            )
        )
    if "export_sql_details" in value:
        import capo_database_migration_service.types.export_sql_details

        out["ExportSqlDetails"] = (
            capo_database_migration_service.types.export_sql_details.serialize_aws_json_1_1(
                value["export_sql_details"]
            )
        )
    if "progress" in value:
        import capo_database_migration_service.types.progress

        out["Progress"] = (
            capo_database_migration_service.types.progress.serialize_aws_json_1_1(
                value["progress"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SchemaConversionRequest:
    out: SchemaConversionRequest = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    if "RequestIdentifier" in data:
        out["request_identifier"] = data["RequestIdentifier"]
    if "MigrationProjectArn" in data:
        out["migration_project_arn"] = data["MigrationProjectArn"]
    if "Error" in data:
        import capo_database_migration_service.types.error_details

        out["error"] = (
            capo_database_migration_service.types.error_details.deserialize_aws_json_1_1(
                data["Error"]
            )
        )
    if "ExportSqlDetails" in data:
        import capo_database_migration_service.types.export_sql_details

        out["export_sql_details"] = (
            capo_database_migration_service.types.export_sql_details.deserialize_aws_json_1_1(
                data["ExportSqlDetails"]
            )
        )
    if "Progress" in data:
        import capo_database_migration_service.types.progress

        out["progress"] = (
            capo_database_migration_service.types.progress.deserialize_aws_json_1_1(
                data["Progress"]
            )
        )
    return out
