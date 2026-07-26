"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DatabaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.collectors_list
    import capo_database_migration_service.types.database_instance_software_details_response
    import capo_database_migration_service.types.long_optional
    import capo_database_migration_service.types.server_short_info_response
    import capo_database_migration_service.types.string


class DatabaseResponse(TypedDict, closed=True):
    database_id: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The ID of a database in a Fleet Advisor collector inventory.</p>"""
    database_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name of a database in a Fleet Advisor collector inventory. </p>"""
    ip_address: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The IP address of a database in a Fleet Advisor collector inventory. </p>"""
    number_of_schemas: NotRequired[
        "capo_database_migration_service.types.long_optional.LongOptional"
    ]
    """<p>The number of schemas in a Fleet Advisor collector inventory database. </p>"""
    server: NotRequired[
        "capo_database_migration_service.types.server_short_info_response.ServerShortInfoResponse"
    ]
    """<p>The server name of a database in a Fleet Advisor collector inventory. </p>"""
    software_details: NotRequired[
        "capo_database_migration_service.types.database_instance_software_details_response.DatabaseInstanceSoftwareDetailsResponse"
    ]
    """<p>The software details of a database in a Fleet Advisor collector inventory, such as database engine and version.</p>"""
    collectors: NotRequired[
        "capo_database_migration_service.types.collectors_list.CollectorsList"
    ]
    """<p>A list of collectors associated with the database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseResponse) -> dict:
    out: dict = {}
    if "database_id" in value:
        out["DatabaseId"] = value["database_id"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "number_of_schemas" in value:
        out["NumberOfSchemas"] = value["number_of_schemas"]
    if "server" in value:
        import capo_database_migration_service.types.server_short_info_response

        out["Server"] = (
            capo_database_migration_service.types.server_short_info_response.serialize_aws_json_1_1(
                value["server"]
            )
        )
    if "software_details" in value:
        import capo_database_migration_service.types.database_instance_software_details_response

        out["SoftwareDetails"] = (
            capo_database_migration_service.types.database_instance_software_details_response.serialize_aws_json_1_1(
                value["software_details"]
            )
        )
    if "collectors" in value:
        import capo_database_migration_service.types.collectors_list

        out["Collectors"] = (
            capo_database_migration_service.types.collectors_list.serialize_aws_json_1_1(
                value["collectors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatabaseResponse:
    out: DatabaseResponse = {}  # type: ignore[typeddict-item]
    if "DatabaseId" in data:
        out["database_id"] = data["DatabaseId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    if "NumberOfSchemas" in data:
        out["number_of_schemas"] = data["NumberOfSchemas"]
    if "Server" in data:
        import capo_database_migration_service.types.server_short_info_response

        out["server"] = (
            capo_database_migration_service.types.server_short_info_response.deserialize_aws_json_1_1(
                data["Server"]
            )
        )
    if "SoftwareDetails" in data:
        import capo_database_migration_service.types.database_instance_software_details_response

        out["software_details"] = (
            capo_database_migration_service.types.database_instance_software_details_response.deserialize_aws_json_1_1(
                data["SoftwareDetails"]
            )
        )
    if "Collectors" in data:
        import capo_database_migration_service.types.collectors_list

        out["collectors"] = (
            capo_database_migration_service.types.collectors_list.deserialize_aws_json_1_1(
                data["Collectors"]
            )
        )
    return out
