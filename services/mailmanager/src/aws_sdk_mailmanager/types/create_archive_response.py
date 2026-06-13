"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateArchiveResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.archive_id_string


class CreateArchiveResponse(TypedDict):
    archive_id: "aws_sdk_mailmanager.types.archive_id_string.ArchiveIdString"
    """<p>The unique identifier for the newly created archive.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateArchiveResponse) -> dict:
    out: dict = {}
    out["ArchiveId"] = value["archive_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateArchiveResponse:
    out: CreateArchiveResponse = {}  # type: ignore[typeddict-item]
    if "ArchiveId" in data:
        out["archive_id"] = data["ArchiveId"]
    else:
        raise DeserializationError("CreateArchiveResponse.archive_id required")
    return out
