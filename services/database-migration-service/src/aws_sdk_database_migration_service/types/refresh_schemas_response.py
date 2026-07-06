"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RefreshSchemasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.refresh_schemas_status


class RefreshSchemasResponse(TypedDict, closed=True):
    refresh_schemas_status: NotRequired[
        "aws_sdk_database_migration_service.types.refresh_schemas_status.RefreshSchemasStatus"
    ]
    """<p>The status of the refreshed schema.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RefreshSchemasResponse) -> dict:
    out: dict = {}
    if "refresh_schemas_status" in value:
        import aws_sdk_database_migration_service.types.refresh_schemas_status

        out["RefreshSchemasStatus"] = (
            aws_sdk_database_migration_service.types.refresh_schemas_status.serialize_aws_json_1_1(
                value["refresh_schemas_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RefreshSchemasResponse:
    out: RefreshSchemasResponse = {}  # type: ignore[typeddict-item]
    if "RefreshSchemasStatus" in data:
        import aws_sdk_database_migration_service.types.refresh_schemas_status

        out["refresh_schemas_status"] = (
            aws_sdk_database_migration_service.types.refresh_schemas_status.deserialize_aws_json_1_1(
                data["RefreshSchemasStatus"]
            )
        )
    return out
