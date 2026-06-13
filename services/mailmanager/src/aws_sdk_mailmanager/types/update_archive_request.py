"""Generated from Smithy shape ``com.amazonaws.mailmanager#UpdateArchiveRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.archive_id_string
    import aws_sdk_mailmanager.types.archive_name_string
    import aws_sdk_mailmanager.types.archive_retention


class UpdateArchiveRequest(TypedDict):
    archive_id: "aws_sdk_mailmanager.types.archive_id_string.ArchiveIdString"
    """<p>The identifier of the archive to update.</p>"""
    archive_name: NotRequired[
        "aws_sdk_mailmanager.types.archive_name_string.ArchiveNameString"
    ]
    """<p>A new, unique name for the archive.</p>"""
    retention: NotRequired[
        "aws_sdk_mailmanager.types.archive_retention.ArchiveRetention"
    ]
    """<p>A new retention period for emails in the archive.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateArchiveRequest) -> dict:
    out: dict = {}
    out["ArchiveId"] = value["archive_id"]
    if "archive_name" in value:
        out["ArchiveName"] = value["archive_name"]
    if "retention" in value:
        import aws_sdk_mailmanager.types.archive_retention

        out["Retention"] = (
            aws_sdk_mailmanager.types.archive_retention.serialize_aws_json_1_0(
                value["retention"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateArchiveRequest:
    out: UpdateArchiveRequest = {}  # type: ignore[typeddict-item]
    if "ArchiveId" in data:
        out["archive_id"] = data["ArchiveId"]
    else:
        raise DeserializationError("UpdateArchiveRequest.archive_id required")
    if "ArchiveName" in data:
        out["archive_name"] = data["ArchiveName"]
    if "Retention" in data:
        import aws_sdk_mailmanager.types.archive_retention

        out["retention"] = (
            aws_sdk_mailmanager.types.archive_retention.deserialize_aws_json_1_0(
                data["Retention"]
            )
        )
    return out
