"""Generated from Smithy shape ``com.amazonaws.finspace#GetKxChangesetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.change_requests
    import aws_sdk_finspace.types.changeset_id
    import aws_sdk_finspace.types.changeset_status
    import aws_sdk_finspace.types.database_name
    import aws_sdk_finspace.types.environment_id
    import aws_sdk_finspace.types.error_info
    import aws_sdk_finspace.types.timestamp


class GetKxChangesetResponse(TypedDict):
    changeset_id: NotRequired["aws_sdk_finspace.types.changeset_id.ChangesetId"]
    """<p>A unique identifier for the changeset.</p>"""
    database_name: NotRequired["aws_sdk_finspace.types.database_name.DatabaseName"]
    """<p>The name of the kdb database.</p>"""
    environment_id: NotRequired["aws_sdk_finspace.types.environment_id.EnvironmentId"]
    """<p>A unique identifier for the kdb environment.</p>"""
    change_requests: NotRequired[
        "aws_sdk_finspace.types.change_requests.ChangeRequests"
    ]
    """<p>A list of change request objects that are run in order.</p>"""
    created_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the changeset was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    active_from_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p>Beginning time from which the changeset is active. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    last_modified_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the changeset was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    status: NotRequired["aws_sdk_finspace.types.changeset_status.ChangesetStatus"]
    """<p>Status of the changeset creation process.</p> <ul> <li> <p>Pending – Changeset creation is pending.</p> </li> <li> <p>Processing – Changeset creation is running.</p> </li> <li> <p>Failed – Changeset creation has failed.</p> </li> <li> <p>Complete – Changeset creation has succeeded.</p> </li> </ul>"""
    error_info: NotRequired["aws_sdk_finspace.types.error_info.ErrorInfo"]
    """<p>Provides details in the event of a failed flow, including the error type and the related error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKxChangesetResponse) -> dict:
    out: dict = {}
    if "changeset_id" in value:
        out["changesetId"] = value["changeset_id"]
    if "database_name" in value:
        out["databaseName"] = value["database_name"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "change_requests" in value:
        import aws_sdk_finspace.types.change_requests

        out["changeRequests"] = aws_sdk_finspace.types.change_requests.serialize_json(
            value["change_requests"]
        )
    if "created_timestamp" in value:
        import aws_sdk_finspace.types.timestamp

        out["createdTimestamp"] = aws_sdk_finspace.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "active_from_timestamp" in value:
        import aws_sdk_finspace.types.timestamp

        out["activeFromTimestamp"] = aws_sdk_finspace.types.timestamp.serialize_json(
            value["active_from_timestamp"]
        )
    if "last_modified_timestamp" in value:
        import aws_sdk_finspace.types.timestamp

        out["lastModifiedTimestamp"] = aws_sdk_finspace.types.timestamp.serialize_json(
            value["last_modified_timestamp"]
        )
    if "status" in value:
        import aws_sdk_finspace.types.changeset_status

        out["status"] = aws_sdk_finspace.types.changeset_status.serialize_json(
            value["status"]
        )
    if "error_info" in value:
        import aws_sdk_finspace.types.error_info

        out["errorInfo"] = aws_sdk_finspace.types.error_info.serialize_json(
            value["error_info"]
        )
    return out


def deserialize_json(data: dict) -> GetKxChangesetResponse:
    out: GetKxChangesetResponse = {}  # type: ignore[typeddict-item]
    if "changesetId" in data:
        out["changeset_id"] = data["changesetId"]
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "changeRequests" in data:
        import aws_sdk_finspace.types.change_requests

        out["change_requests"] = (
            aws_sdk_finspace.types.change_requests.deserialize_json(
                data["changeRequests"]
            )
        )
    if "createdTimestamp" in data:
        import aws_sdk_finspace.types.timestamp

        out["created_timestamp"] = aws_sdk_finspace.types.timestamp.deserialize_json(
            data["createdTimestamp"]
        )
    if "activeFromTimestamp" in data:
        import aws_sdk_finspace.types.timestamp

        out["active_from_timestamp"] = (
            aws_sdk_finspace.types.timestamp.deserialize_json(
                data["activeFromTimestamp"]
            )
        )
    if "lastModifiedTimestamp" in data:
        import aws_sdk_finspace.types.timestamp

        out["last_modified_timestamp"] = (
            aws_sdk_finspace.types.timestamp.deserialize_json(
                data["lastModifiedTimestamp"]
            )
        )
    if "status" in data:
        import aws_sdk_finspace.types.changeset_status

        out["status"] = aws_sdk_finspace.types.changeset_status.deserialize_json(
            data["status"]
        )
    if "errorInfo" in data:
        import aws_sdk_finspace.types.error_info

        out["error_info"] = aws_sdk_finspace.types.error_info.deserialize_json(
            data["errorInfo"]
        )
    return out
