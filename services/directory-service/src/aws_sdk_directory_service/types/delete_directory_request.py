"""Generated from Smithy shape ``com.amazonaws.directoryservice#DeleteDirectoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id


class DeleteDirectoryRequest(TypedDict, closed=True):
    directory_id: "aws_sdk_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDirectoryRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDirectoryRequest:
    out: DeleteDirectoryRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("DeleteDirectoryRequest.directory_id required")
    return out
