"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SchemaShortInfoResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class SchemaShortInfoResponse(TypedDict):
    schema_id: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The ID of a schema in a Fleet Advisor collector inventory.</p>"""
    schema_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The name of a schema in a Fleet Advisor collector inventory.</p>"""
    database_id: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The ID of a database in a Fleet Advisor collector inventory.</p>"""
    database_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The name of a database in a Fleet Advisor collector inventory.</p>"""
    database_ip_address: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The IP address of a database in a Fleet Advisor collector inventory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaShortInfoResponse) -> dict:
    out: dict = {}
    if "schema_id" in value:
        out["SchemaId"] = value["schema_id"]
    if "schema_name" in value:
        out["SchemaName"] = value["schema_name"]
    if "database_id" in value:
        out["DatabaseId"] = value["database_id"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "database_ip_address" in value:
        out["DatabaseIpAddress"] = value["database_ip_address"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SchemaShortInfoResponse:
    out: SchemaShortInfoResponse = {}  # type: ignore[typeddict-item]
    if "SchemaId" in data:
        out["schema_id"] = data["SchemaId"]
    if "SchemaName" in data:
        out["schema_name"] = data["SchemaName"]
    if "DatabaseId" in data:
        out["database_id"] = data["DatabaseId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "DatabaseIpAddress" in data:
        out["database_ip_address"] = data["DatabaseIpAddress"]
    return out
