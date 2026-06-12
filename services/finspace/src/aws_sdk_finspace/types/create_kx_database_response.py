"""Generated from Smithy shape ``com.amazonaws.finspace#CreateKxDatabaseResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.database_arn
    import aws_sdk_finspace.types.database_name
    import aws_sdk_finspace.types.description
    import aws_sdk_finspace.types.environment_id
    import aws_sdk_finspace.types.timestamp


class CreateKxDatabaseResponse(TypedDict):
    database_name: NotRequired["aws_sdk_finspace.types.database_name.DatabaseName"]
    """<p>The name of the kdb database.</p>"""
    database_arn: NotRequired["aws_sdk_finspace.types.database_arn.DatabaseArn"]
    """<p>The ARN identifier of the database.</p>"""
    environment_id: NotRequired["aws_sdk_finspace.types.environment_id.EnvironmentId"]
    """<p>A unique identifier for the kdb environment.</p>"""
    description: NotRequired["aws_sdk_finspace.types.description.Description"]
    """<p>A description of the database.</p>"""
    created_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the database is created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    last_modified_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p>The last time that the database was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKxDatabaseResponse) -> dict:
    out: dict = {}
    if "database_name" in value:
        out["databaseName"] = value["database_name"]
    if "database_arn" in value:
        out["databaseArn"] = value["database_arn"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_timestamp" in value:
        import aws_sdk_finspace.types.timestamp

        out["createdTimestamp"] = aws_sdk_finspace.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "last_modified_timestamp" in value:
        import aws_sdk_finspace.types.timestamp

        out["lastModifiedTimestamp"] = aws_sdk_finspace.types.timestamp.serialize_json(
            value["last_modified_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> CreateKxDatabaseResponse:
    out: CreateKxDatabaseResponse = {}  # type: ignore[typeddict-item]
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    if "databaseArn" in data:
        out["database_arn"] = data["databaseArn"]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "description" in data:
        out["description"] = data["description"]
    if "createdTimestamp" in data:
        import aws_sdk_finspace.types.timestamp

        out["created_timestamp"] = aws_sdk_finspace.types.timestamp.deserialize_json(
            data["createdTimestamp"]
        )
    if "lastModifiedTimestamp" in data:
        import aws_sdk_finspace.types.timestamp

        out["last_modified_timestamp"] = (
            aws_sdk_finspace.types.timestamp.deserialize_json(
                data["lastModifiedTimestamp"]
            )
        )
    return out
