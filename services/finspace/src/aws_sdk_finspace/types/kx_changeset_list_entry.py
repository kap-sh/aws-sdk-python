"""Generated from Smithy shape ``com.amazonaws.finspace#KxChangesetListEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.changeset_id
    import aws_sdk_finspace.types.changeset_status
    import aws_sdk_finspace.types.timestamp


class KxChangesetListEntry(TypedDict):
    changeset_id: NotRequired["aws_sdk_finspace.types.changeset_id.ChangesetId"]
    """<p>A unique identifier for the changeset.</p>"""
    created_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the changeset was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    active_from_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p>Beginning time from which the changeset is active. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    last_modified_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the changeset was modified. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    status: NotRequired["aws_sdk_finspace.types.changeset_status.ChangesetStatus"]
    """<p> Status of the changeset.</p> <ul> <li> <p>Pending – Changeset creation is pending.</p> </li> <li> <p>Processing – Changeset creation is running.</p> </li> <li> <p>Failed – Changeset creation has failed.</p> </li> <li> <p>Complete – Changeset creation has succeeded.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxChangesetListEntry) -> dict:
    out: dict = {}
    if "changeset_id" in value:
        out["changesetId"] = value["changeset_id"]
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
    return out


def deserialize_json(data: dict) -> KxChangesetListEntry:
    out: KxChangesetListEntry = {}  # type: ignore[typeddict-item]
    if "changesetId" in data:
        out["changeset_id"] = data["changesetId"]
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
    return out
