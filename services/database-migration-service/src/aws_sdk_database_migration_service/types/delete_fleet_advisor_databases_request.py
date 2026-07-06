"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteFleetAdvisorDatabasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string_list


class DeleteFleetAdvisorDatabasesRequest(TypedDict, closed=True):
    database_ids: "aws_sdk_database_migration_service.types.string_list.StringList"
    """<p>The IDs of the Fleet Advisor collector databases to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFleetAdvisorDatabasesRequest) -> dict:
    out: dict = {}
    import aws_sdk_database_migration_service.types.string_list

    out["DatabaseIds"] = (
        aws_sdk_database_migration_service.types.string_list.serialize_aws_json_1_1(
            value["database_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFleetAdvisorDatabasesRequest:
    out: DeleteFleetAdvisorDatabasesRequest = {}  # type: ignore[typeddict-item]
    if "DatabaseIds" in data:
        import aws_sdk_database_migration_service.types.string_list

        out["database_ids"] = (
            aws_sdk_database_migration_service.types.string_list.deserialize_aws_json_1_1(
                data["DatabaseIds"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteFleetAdvisorDatabasesRequest.database_ids required"
        )
    return out
