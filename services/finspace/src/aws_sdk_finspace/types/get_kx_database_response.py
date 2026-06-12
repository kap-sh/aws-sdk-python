"""Generated from Smithy shape ``com.amazonaws.finspace#GetKxDatabaseResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.changeset_id
    import aws_sdk_finspace.types.database_arn
    import aws_sdk_finspace.types.database_name
    import aws_sdk_finspace.types.description
    import aws_sdk_finspace.types.environment_id
    import aws_sdk_finspace.types.num_bytes
    import aws_sdk_finspace.types.num_changesets
    import aws_sdk_finspace.types.num_files
    import aws_sdk_finspace.types.timestamp


class GetKxDatabaseResponse(TypedDict):
    database_name: NotRequired["aws_sdk_finspace.types.database_name.DatabaseName"]
    """<p>The name of the kdb database for which the information is retrieved.</p>"""
    database_arn: NotRequired["aws_sdk_finspace.types.database_arn.DatabaseArn"]
    """<p>The ARN identifier of the database.</p>"""
    environment_id: NotRequired["aws_sdk_finspace.types.environment_id.EnvironmentId"]
    """<p>A unique identifier for the kdb environment.</p>"""
    description: NotRequired["aws_sdk_finspace.types.description.Description"]
    """<p>A description of the database.</p>"""
    created_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the database is created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    last_modified_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p>The last time that the database was modified. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    last_completed_changeset_id: NotRequired[
        "aws_sdk_finspace.types.changeset_id.ChangesetId"
    ]
    """<p>A unique identifier for the changeset.</p>"""
    num_bytes: "aws_sdk_finspace.types.num_bytes.numBytes"
    """<p>The total number of bytes in the database.</p>"""
    num_changesets: "aws_sdk_finspace.types.num_changesets.numChangesets"
    """<p>The total number of changesets in the database.</p>"""
    num_files: "aws_sdk_finspace.types.num_files.numFiles"
    """<p>The total number of files in the database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKxDatabaseResponse) -> dict:
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
    if "last_completed_changeset_id" in value:
        out["lastCompletedChangesetId"] = value["last_completed_changeset_id"]
    out["numBytes"] = value.get("num_bytes", 0)
    out["numChangesets"] = value.get("num_changesets", 0)
    out["numFiles"] = value.get("num_files", 0)
    return out


def deserialize_json(data: dict) -> GetKxDatabaseResponse:
    out: GetKxDatabaseResponse = {}  # type: ignore[typeddict-item]
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
    if "lastCompletedChangesetId" in data:
        out["last_completed_changeset_id"] = data["lastCompletedChangesetId"]
    if "numBytes" in data:
        out["num_bytes"] = data["numBytes"]
    else:
        out["num_bytes"] = 0
    if "numChangesets" in data:
        out["num_changesets"] = data["numChangesets"]
    else:
        out["num_changesets"] = 0
    if "numFiles" in data:
        out["num_files"] = data["numFiles"]
    else:
        out["num_files"] = 0
    return out
