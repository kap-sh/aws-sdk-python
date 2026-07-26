"""Generated from Smithy shape ``com.amazonaws.migrationhub#DescribeMigrationTaskResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub.types.migration_task


class DescribeMigrationTaskResult(TypedDict, closed=True):
    migration_task: NotRequired["capo_migration_hub.types.migration_task.MigrationTask"]
    """<p>Object encapsulating information about the migration task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMigrationTaskResult) -> dict:
    out: dict = {}
    if "migration_task" in value:
        import capo_migration_hub.types.migration_task

        out["MigrationTask"] = (
            capo_migration_hub.types.migration_task.serialize_aws_json_1_1(
                value["migration_task"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMigrationTaskResult:
    out: DescribeMigrationTaskResult = {}  # type: ignore[typeddict-item]
    if "MigrationTask" in data:
        import capo_migration_hub.types.migration_task

        out["migration_task"] = (
            capo_migration_hub.types.migration_task.deserialize_aws_json_1_1(
                data["MigrationTask"]
            )
        )
    return out
