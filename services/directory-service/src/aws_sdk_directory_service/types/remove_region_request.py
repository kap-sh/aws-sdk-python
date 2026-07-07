"""Generated from Smithy shape ``com.amazonaws.directoryservice#RemoveRegionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id


class RemoveRegionRequest(TypedDict, closed=True):
    directory_id: "aws_sdk_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory for which you want to remove Region replication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveRegionRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveRegionRequest:
    out: RemoveRegionRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("RemoveRegionRequest.directory_id required")
    return out
