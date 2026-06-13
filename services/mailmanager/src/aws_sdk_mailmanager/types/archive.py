"""Generated from Smithy shape ``com.amazonaws.mailmanager#Archive``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mailmanager.types.archive_id_string
    import aws_sdk_mailmanager.types.archive_name_string
    import aws_sdk_mailmanager.types.archive_state


class Archive(TypedDict):
    archive_id: "aws_sdk_mailmanager.types.archive_id_string.ArchiveIdString"
    """<p>The unique identifier of the archive.</p>"""
    archive_name: NotRequired[
        "aws_sdk_mailmanager.types.archive_name_string.ArchiveNameString"
    ]
    """<p>The unique name assigned to the archive.</p>"""
    archive_state: NotRequired["aws_sdk_mailmanager.types.archive_state.ArchiveState"]
    """<p>The current state of the archive:</p> <ul> <li> <p> <code>ACTIVE</code> – The archive is ready and available for use. </p> </li> <li> <p> <code>PENDING_DELETION</code> – The archive has been marked for deletion and will be permanently deleted in 30 days. No further modifications can be made in this state. </p> </li> </ul>"""
    last_updated_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the archive was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Archive) -> dict:
    out: dict = {}
    out["ArchiveId"] = value["archive_id"]
    if "archive_name" in value:
        out["ArchiveName"] = value["archive_name"]
    if "archive_state" in value:
        import aws_sdk_mailmanager.types.archive_state

        out["ArchiveState"] = (
            aws_sdk_mailmanager.types.archive_state.serialize_aws_json_1_0(
                value["archive_state"]
            )
        )
    if "last_updated_timestamp" in value:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["LastUpdatedTimestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_updated_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Archive:
    out: Archive = {}  # type: ignore[typeddict-item]
    if "ArchiveId" in data:
        out["archive_id"] = data["ArchiveId"]
    else:
        raise DeserializationError("Archive.archive_id required")
    if "ArchiveName" in data:
        out["archive_name"] = data["ArchiveName"]
    if "ArchiveState" in data:
        import aws_sdk_mailmanager.types.archive_state

        out["archive_state"] = (
            aws_sdk_mailmanager.types.archive_state.deserialize_aws_json_1_0(
                data["ArchiveState"]
            )
        )
    if "LastUpdatedTimestamp" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["LastUpdatedTimestamp"]
            )
        )
    return out
