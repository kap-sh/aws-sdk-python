"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.connection


class DeleteConnectionResponse(TypedDict, closed=True):
    connection: NotRequired[
        "aws_sdk_database_migration_service.types.connection.Connection"
    ]
    """<p>The connection that is being deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteConnectionResponse) -> dict:
    out: dict = {}
    if "connection" in value:
        import aws_sdk_database_migration_service.types.connection

        out["Connection"] = (
            aws_sdk_database_migration_service.types.connection.serialize_aws_json_1_1(
                value["connection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteConnectionResponse:
    out: DeleteConnectionResponse = {}  # type: ignore[typeddict-item]
    if "Connection" in data:
        import aws_sdk_database_migration_service.types.connection

        out["connection"] = (
            aws_sdk_database_migration_service.types.connection.deserialize_aws_json_1_1(
                data["Connection"]
            )
        )
    return out
