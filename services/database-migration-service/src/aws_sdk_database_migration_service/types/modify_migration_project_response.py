"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyMigrationProjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.migration_project


class ModifyMigrationProjectResponse(TypedDict, closed=True):
    migration_project: NotRequired[
        "aws_sdk_database_migration_service.types.migration_project.MigrationProject"
    ]
    """<p>The migration project that was modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyMigrationProjectResponse) -> dict:
    out: dict = {}
    if "migration_project" in value:
        import aws_sdk_database_migration_service.types.migration_project

        out["MigrationProject"] = (
            aws_sdk_database_migration_service.types.migration_project.serialize_aws_json_1_1(
                value["migration_project"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyMigrationProjectResponse:
    out: ModifyMigrationProjectResponse = {}  # type: ignore[typeddict-item]
    if "MigrationProject" in data:
        import aws_sdk_database_migration_service.types.migration_project

        out["migration_project"] = (
            aws_sdk_database_migration_service.types.migration_project.deserialize_aws_json_1_1(
                data["MigrationProject"]
            )
        )
    return out
