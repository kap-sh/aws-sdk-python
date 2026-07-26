"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CollectorHealthCheck``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.collector_status


class CollectorHealthCheck(TypedDict, closed=True):
    collector_status: NotRequired[
        "capo_database_migration_service.types.collector_status.CollectorStatus"
    ]
    """<p>The status of the Fleet Advisor collector.</p>"""
    local_collector_s3_access: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Whether the local collector can access its Amazon S3 bucket.</p>"""
    web_collector_s3_access: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Whether the web collector can access its Amazon S3 bucket.</p>"""
    web_collector_granted_role_based_access: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Whether the role that you provided when creating the Fleet Advisor collector has sufficient permissions to access the Fleet Advisor web collector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CollectorHealthCheck) -> dict:
    out: dict = {}
    if "collector_status" in value:
        import capo_database_migration_service.types.collector_status

        out["CollectorStatus"] = (
            capo_database_migration_service.types.collector_status.serialize_aws_json_1_1(
                value["collector_status"]
            )
        )
    if "local_collector_s3_access" in value:
        out["LocalCollectorS3Access"] = value["local_collector_s3_access"]
    if "web_collector_s3_access" in value:
        out["WebCollectorS3Access"] = value["web_collector_s3_access"]
    if "web_collector_granted_role_based_access" in value:
        out["WebCollectorGrantedRoleBasedAccess"] = value[
            "web_collector_granted_role_based_access"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> CollectorHealthCheck:
    out: CollectorHealthCheck = {}  # type: ignore[typeddict-item]
    if "CollectorStatus" in data:
        import capo_database_migration_service.types.collector_status

        out["collector_status"] = (
            capo_database_migration_service.types.collector_status.deserialize_aws_json_1_1(
                data["CollectorStatus"]
            )
        )
    if "LocalCollectorS3Access" in data:
        out["local_collector_s3_access"] = data["LocalCollectorS3Access"]
    if "WebCollectorS3Access" in data:
        out["web_collector_s3_access"] = data["WebCollectorS3Access"]
    if "WebCollectorGrantedRoleBasedAccess" in data:
        out["web_collector_granted_role_based_access"] = data[
            "WebCollectorGrantedRoleBasedAccess"
        ]
    return out
