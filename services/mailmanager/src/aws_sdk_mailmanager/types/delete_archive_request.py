"""Generated from Smithy shape ``com.amazonaws.mailmanager#DeleteArchiveRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.archive_id_string


class DeleteArchiveRequest(TypedDict):
    archive_id: "aws_sdk_mailmanager.types.archive_id_string.ArchiveIdString"
    """<p>The identifier of the archive to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteArchiveRequest) -> dict:
    out: dict = {}
    out["ArchiveId"] = value["archive_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteArchiveRequest:
    out: DeleteArchiveRequest = {}  # type: ignore[typeddict-item]
    if "ArchiveId" in data:
        out["archive_id"] = data["ArchiveId"]
    else:
        raise DeserializationError("DeleteArchiveRequest.archive_id required")
    return out
