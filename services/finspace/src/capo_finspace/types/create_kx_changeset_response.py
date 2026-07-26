"""Generated from Smithy shape ``com.amazonaws.finspace#CreateKxChangesetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.change_requests
    import capo_finspace.types.changeset_id
    import capo_finspace.types.changeset_status
    import capo_finspace.types.database_name
    import capo_finspace.types.environment_id
    import capo_finspace.types.error_info
    import capo_finspace.types.timestamp


class CreateKxChangesetResponse(TypedDict, closed=True):
    changeset_id: NotRequired["capo_finspace.types.changeset_id.ChangesetId"]
    """<p>A unique identifier for the changeset.</p>"""
    database_name: NotRequired["capo_finspace.types.database_name.DatabaseName"]
    """<p>The name of the kdb database.</p>"""
    environment_id: NotRequired["capo_finspace.types.environment_id.EnvironmentId"]
    """<p>A unique identifier for the kdb environment.</p>"""
    change_requests: NotRequired["capo_finspace.types.change_requests.ChangeRequests"]
    """<p>A list of change requests.</p>"""
    created_timestamp: NotRequired["capo_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the changeset was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    last_modified_timestamp: NotRequired["capo_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the changeset was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    status: NotRequired["capo_finspace.types.changeset_status.ChangesetStatus"]
    """<p>Status of the changeset creation process.</p> <ul> <li> <p>Pending – Changeset creation is pending.</p> </li> <li> <p>Processing – Changeset creation is running.</p> </li> <li> <p>Failed – Changeset creation has failed.</p> </li> <li> <p>Complete – Changeset creation has succeeded.</p> </li> </ul>"""
    error_info: NotRequired["capo_finspace.types.error_info.ErrorInfo"]
    """<p>The details of the error that you receive when creating a changeset. It consists of the type of error and the error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKxChangesetResponse) -> dict:
    out: dict = {}
    if "changeset_id" in value:
        out["changesetId"] = value["changeset_id"]
    if "database_name" in value:
        out["databaseName"] = value["database_name"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "change_requests" in value:
        import capo_finspace.types.change_requests

        out["changeRequests"] = capo_finspace.types.change_requests.serialize_json(
            value["change_requests"]
        )
    if "created_timestamp" in value:
        import capo_finspace.types.timestamp

        out["createdTimestamp"] = capo_finspace.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "last_modified_timestamp" in value:
        import capo_finspace.types.timestamp

        out["lastModifiedTimestamp"] = capo_finspace.types.timestamp.serialize_json(
            value["last_modified_timestamp"]
        )
    if "status" in value:
        import capo_finspace.types.changeset_status

        out["status"] = capo_finspace.types.changeset_status.serialize_json(
            value["status"]
        )
    if "error_info" in value:
        import capo_finspace.types.error_info

        out["errorInfo"] = capo_finspace.types.error_info.serialize_json(
            value["error_info"]
        )
    return out


def deserialize_json(data: dict) -> CreateKxChangesetResponse:
    out: CreateKxChangesetResponse = {}  # type: ignore[typeddict-item]
    if "changesetId" in data:
        out["changeset_id"] = data["changesetId"]
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "changeRequests" in data:
        import capo_finspace.types.change_requests

        out["change_requests"] = capo_finspace.types.change_requests.deserialize_json(
            data["changeRequests"]
        )
    if "createdTimestamp" in data:
        import capo_finspace.types.timestamp

        out["created_timestamp"] = capo_finspace.types.timestamp.deserialize_json(
            data["createdTimestamp"]
        )
    if "lastModifiedTimestamp" in data:
        import capo_finspace.types.timestamp

        out["last_modified_timestamp"] = capo_finspace.types.timestamp.deserialize_json(
            data["lastModifiedTimestamp"]
        )
    if "status" in data:
        import capo_finspace.types.changeset_status

        out["status"] = capo_finspace.types.changeset_status.deserialize_json(
            data["status"]
        )
    if "errorInfo" in data:
        import capo_finspace.types.error_info

        out["error_info"] = capo_finspace.types.error_info.deserialize_json(
            data["errorInfo"]
        )
    return out
