"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DatabaseShortInfoResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class DatabaseShortInfoResponse(TypedDict):
    database_id: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The ID of a database in a Fleet Advisor collector inventory.</p>"""
    database_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The name of a database in a Fleet Advisor collector inventory.</p>"""
    database_ip_address: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The IP address of a database in a Fleet Advisor collector inventory.</p>"""
    database_engine: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The database engine of a database in a Fleet Advisor collector inventory, for example <code>PostgreSQL</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseShortInfoResponse) -> dict:
    out: dict = {}
    if "database_id" in value:
        out["DatabaseId"] = value["database_id"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "database_ip_address" in value:
        out["DatabaseIpAddress"] = value["database_ip_address"]
    if "database_engine" in value:
        out["DatabaseEngine"] = value["database_engine"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DatabaseShortInfoResponse:
    out: DatabaseShortInfoResponse = {}  # type: ignore[typeddict-item]
    if "DatabaseId" in data:
        out["database_id"] = data["DatabaseId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "DatabaseIpAddress" in data:
        out["database_ip_address"] = data["DatabaseIpAddress"]
    if "DatabaseEngine" in data:
        out["database_engine"] = data["DatabaseEngine"]
    return out
