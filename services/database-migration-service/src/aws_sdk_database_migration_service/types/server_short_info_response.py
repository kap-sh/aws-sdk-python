"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ServerShortInfoResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class ServerShortInfoResponse(TypedDict):
    server_id: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The ID of a server in a Fleet Advisor collector inventory.</p>"""
    ip_address: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The IP address of a server in a Fleet Advisor collector inventory.</p>"""
    server_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The name address of a server in a Fleet Advisor collector inventory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServerShortInfoResponse) -> dict:
    out: dict = {}
    if "server_id" in value:
        out["ServerId"] = value["server_id"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "server_name" in value:
        out["ServerName"] = value["server_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServerShortInfoResponse:
    out: ServerShortInfoResponse = {}  # type: ignore[typeddict-item]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    if "ServerName" in data:
        out["server_name"] = data["ServerName"]
    return out
