"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#TestConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.connection


class TestConnectionResponse(TypedDict, closed=True):
    connection: NotRequired[
        "aws_sdk_database_migration_service.types.connection.Connection"
    ]
    """<p>The connection tested.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestConnectionResponse) -> dict:
    out: dict = {}
    if "connection" in value:
        import aws_sdk_database_migration_service.types.connection

        out["Connection"] = (
            aws_sdk_database_migration_service.types.connection.serialize_aws_json_1_1(
                value["connection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestConnectionResponse:
    out: TestConnectionResponse = {}  # type: ignore[typeddict-item]
    if "Connection" in data:
        import aws_sdk_database_migration_service.types.connection

        out["connection"] = (
            aws_sdk_database_migration_service.types.connection.deserialize_aws_json_1_1(
                data["Connection"]
            )
        )
    return out
