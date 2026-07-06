"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SchemaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.database_short_info_response
    import aws_sdk_database_migration_service.types.double_optional
    import aws_sdk_database_migration_service.types.long_optional
    import aws_sdk_database_migration_service.types.schema_short_info_response
    import aws_sdk_database_migration_service.types.server_short_info_response
    import aws_sdk_database_migration_service.types.string


class SchemaResponse(TypedDict, closed=True):
    code_line_count: NotRequired[
        "aws_sdk_database_migration_service.types.long_optional.LongOptional"
    ]
    """<p>The number of lines of code in a schema in a Fleet Advisor collector inventory.</p>"""
    code_size: NotRequired[
        "aws_sdk_database_migration_service.types.long_optional.LongOptional"
    ]
    """<p>The size level of the code in a schema in a Fleet Advisor collector inventory.</p>"""
    complexity: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The complexity level of the code in a schema in a Fleet Advisor collector inventory.</p>"""
    server: NotRequired[
        "aws_sdk_database_migration_service.types.server_short_info_response.ServerShortInfoResponse"
    ]
    """<p>The database server for a schema in a Fleet Advisor collector inventory.</p>"""
    database_instance: NotRequired[
        "aws_sdk_database_migration_service.types.database_short_info_response.DatabaseShortInfoResponse"
    ]
    """<p>The database for a schema in a Fleet Advisor collector inventory.</p>"""
    schema_id: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The ID of a schema in a Fleet Advisor collector inventory.</p>"""
    schema_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The name of a schema in a Fleet Advisor collector inventory.</p>"""
    original_schema: NotRequired[
        "aws_sdk_database_migration_service.types.schema_short_info_response.SchemaShortInfoResponse"
    ]
    similarity: NotRequired[
        "aws_sdk_database_migration_service.types.double_optional.DoubleOptional"
    ]
    """<p>The similarity value for a schema in a Fleet Advisor collector inventory. A higher similarity value indicates that a schema is likely to be a duplicate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaResponse) -> dict:
    out: dict = {}
    if "code_line_count" in value:
        out["CodeLineCount"] = value["code_line_count"]
    if "code_size" in value:
        out["CodeSize"] = value["code_size"]
    if "complexity" in value:
        out["Complexity"] = value["complexity"]
    if "server" in value:
        import aws_sdk_database_migration_service.types.server_short_info_response

        out["Server"] = (
            aws_sdk_database_migration_service.types.server_short_info_response.serialize_aws_json_1_1(
                value["server"]
            )
        )
    if "database_instance" in value:
        import aws_sdk_database_migration_service.types.database_short_info_response

        out["DatabaseInstance"] = (
            aws_sdk_database_migration_service.types.database_short_info_response.serialize_aws_json_1_1(
                value["database_instance"]
            )
        )
    if "schema_id" in value:
        out["SchemaId"] = value["schema_id"]
    if "schema_name" in value:
        out["SchemaName"] = value["schema_name"]
    if "original_schema" in value:
        import aws_sdk_database_migration_service.types.schema_short_info_response

        out["OriginalSchema"] = (
            aws_sdk_database_migration_service.types.schema_short_info_response.serialize_aws_json_1_1(
                value["original_schema"]
            )
        )
    if "similarity" in value:
        out["Similarity"] = value["similarity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SchemaResponse:
    out: SchemaResponse = {}  # type: ignore[typeddict-item]
    if "CodeLineCount" in data:
        out["code_line_count"] = data["CodeLineCount"]
    if "CodeSize" in data:
        out["code_size"] = data["CodeSize"]
    if "Complexity" in data:
        out["complexity"] = data["Complexity"]
    if "Server" in data:
        import aws_sdk_database_migration_service.types.server_short_info_response

        out["server"] = (
            aws_sdk_database_migration_service.types.server_short_info_response.deserialize_aws_json_1_1(
                data["Server"]
            )
        )
    if "DatabaseInstance" in data:
        import aws_sdk_database_migration_service.types.database_short_info_response

        out["database_instance"] = (
            aws_sdk_database_migration_service.types.database_short_info_response.deserialize_aws_json_1_1(
                data["DatabaseInstance"]
            )
        )
    if "SchemaId" in data:
        out["schema_id"] = data["SchemaId"]
    if "SchemaName" in data:
        out["schema_name"] = data["SchemaName"]
    if "OriginalSchema" in data:
        import aws_sdk_database_migration_service.types.schema_short_info_response

        out["original_schema"] = (
            aws_sdk_database_migration_service.types.schema_short_info_response.deserialize_aws_json_1_1(
                data["OriginalSchema"]
            )
        )
    if "Similarity" in data:
        out["similarity"] = data["Similarity"]
    return out
