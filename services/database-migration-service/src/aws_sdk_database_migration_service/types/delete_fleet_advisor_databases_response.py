"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteFleetAdvisorDatabasesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string_list


class DeleteFleetAdvisorDatabasesResponse(TypedDict):
    database_ids: NotRequired[
        "aws_sdk_database_migration_service.types.string_list.StringList"
    ]
    """<p>The IDs of the databases that the operation deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFleetAdvisorDatabasesResponse) -> dict:
    out: dict = {}
    if "database_ids" in value:
        import aws_sdk_database_migration_service.types.string_list

        out["DatabaseIds"] = (
            aws_sdk_database_migration_service.types.string_list.serialize_aws_json_1_1(
                value["database_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFleetAdvisorDatabasesResponse:
    out: DeleteFleetAdvisorDatabasesResponse = {}  # type: ignore[typeddict-item]
    if "DatabaseIds" in data:
        import aws_sdk_database_migration_service.types.string_list

        out["database_ids"] = (
            aws_sdk_database_migration_service.types.string_list.deserialize_aws_json_1_1(
                data["DatabaseIds"]
            )
        )
    return out
