"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateMigrationProjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.migration_project


class CreateMigrationProjectResponse(TypedDict, closed=True):
    migration_project: NotRequired[
        "aws_sdk_database_migration_service.types.migration_project.MigrationProject"
    ]
    """<p>The migration project that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMigrationProjectResponse) -> dict:
    out: dict = {}
    if "migration_project" in value:
        import aws_sdk_database_migration_service.types.migration_project

        out["MigrationProject"] = (
            aws_sdk_database_migration_service.types.migration_project.serialize_aws_json_1_1(
                value["migration_project"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMigrationProjectResponse:
    out: CreateMigrationProjectResponse = {}  # type: ignore[typeddict-item]
    if "MigrationProject" in data:
        import aws_sdk_database_migration_service.types.migration_project

        out["migration_project"] = (
            aws_sdk_database_migration_service.types.migration_project.deserialize_aws_json_1_1(
                data["MigrationProject"]
            )
        )
    return out
