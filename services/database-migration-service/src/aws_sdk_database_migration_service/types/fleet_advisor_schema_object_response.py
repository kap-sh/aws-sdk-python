"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#FleetAdvisorSchemaObjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.long_optional
    import aws_sdk_database_migration_service.types.string


class FleetAdvisorSchemaObjectResponse(TypedDict, closed=True):
    schema_id: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The ID of a schema object in a Fleet Advisor collector inventory.</p>"""
    object_type: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The type of the schema object, as reported by the database engine. Examples include the following:</p> <ul> <li> <p> <code>function</code> </p> </li> <li> <p> <code>trigger</code> </p> </li> <li> <p> <code>SYSTEM_TABLE</code> </p> </li> <li> <p> <code>QUEUE</code> </p> </li> </ul>"""
    number_of_objects: NotRequired[
        "aws_sdk_database_migration_service.types.long_optional.LongOptional"
    ]
    """<p>The number of objects in a schema object in a Fleet Advisor collector inventory.</p>"""
    code_line_count: NotRequired[
        "aws_sdk_database_migration_service.types.long_optional.LongOptional"
    ]
    """<p>The number of lines of code in a schema object in a Fleet Advisor collector inventory.</p>"""
    code_size: NotRequired[
        "aws_sdk_database_migration_service.types.long_optional.LongOptional"
    ]
    """<p>The size level of the code in a schema object in a Fleet Advisor collector inventory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetAdvisorSchemaObjectResponse) -> dict:
    out: dict = {}
    if "schema_id" in value:
        out["SchemaId"] = value["schema_id"]
    if "object_type" in value:
        out["ObjectType"] = value["object_type"]
    if "number_of_objects" in value:
        out["NumberOfObjects"] = value["number_of_objects"]
    if "code_line_count" in value:
        out["CodeLineCount"] = value["code_line_count"]
    if "code_size" in value:
        out["CodeSize"] = value["code_size"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FleetAdvisorSchemaObjectResponse:
    out: FleetAdvisorSchemaObjectResponse = {}  # type: ignore[typeddict-item]
    if "SchemaId" in data:
        out["schema_id"] = data["SchemaId"]
    if "ObjectType" in data:
        out["object_type"] = data["ObjectType"]
    if "NumberOfObjects" in data:
        out["number_of_objects"] = data["NumberOfObjects"]
    if "CodeLineCount" in data:
        out["code_line_count"] = data["CodeLineCount"]
    if "CodeSize" in data:
        out["code_size"] = data["CodeSize"]
    return out
