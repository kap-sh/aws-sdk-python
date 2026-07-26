"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteMigrationProjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.migration_project


class DeleteMigrationProjectResponse(TypedDict, closed=True):
    migration_project: NotRequired[
        "capo_database_migration_service.types.migration_project.MigrationProject"
    ]
    """<p>The migration project that was deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMigrationProjectResponse) -> dict:
    out: dict = {}
    if "migration_project" in value:
        import capo_database_migration_service.types.migration_project

        out["MigrationProject"] = (
            capo_database_migration_service.types.migration_project.serialize_aws_json_1_1(
                value["migration_project"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMigrationProjectResponse:
    out: DeleteMigrationProjectResponse = {}  # type: ignore[typeddict-item]
    if "MigrationProject" in data:
        import capo_database_migration_service.types.migration_project

        out["migration_project"] = (
            capo_database_migration_service.types.migration_project.deserialize_aws_json_1_1(
                data["MigrationProject"]
            )
        )
    return out
