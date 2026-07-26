"""Generated from Smithy shape ``com.amazonaws.finspace#UpdateKxDatabaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.database_name
    import capo_finspace.types.description
    import capo_finspace.types.environment_id
    import capo_finspace.types.timestamp


class UpdateKxDatabaseResponse(TypedDict, closed=True):
    database_name: NotRequired["capo_finspace.types.database_name.DatabaseName"]
    """<p>The name of the kdb database.</p>"""
    environment_id: NotRequired["capo_finspace.types.environment_id.EnvironmentId"]
    """<p>A unique identifier for the kdb environment.</p>"""
    description: NotRequired["capo_finspace.types.description.Description"]
    """<p>A description of the database.</p>"""
    last_modified_timestamp: NotRequired["capo_finspace.types.timestamp.Timestamp"]
    """<p>The last time that the database was modified. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKxDatabaseResponse) -> dict:
    out: dict = {}
    if "database_name" in value:
        out["databaseName"] = value["database_name"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "last_modified_timestamp" in value:
        import capo_finspace.types.timestamp

        out["lastModifiedTimestamp"] = capo_finspace.types.timestamp.serialize_json(
            value["last_modified_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> UpdateKxDatabaseResponse:
    out: UpdateKxDatabaseResponse = {}  # type: ignore[typeddict-item]
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "description" in data:
        out["description"] = data["description"]
    if "lastModifiedTimestamp" in data:
        import capo_finspace.types.timestamp

        out["last_modified_timestamp"] = capo_finspace.types.timestamp.deserialize_json(
            data["lastModifiedTimestamp"]
        )
    return out
