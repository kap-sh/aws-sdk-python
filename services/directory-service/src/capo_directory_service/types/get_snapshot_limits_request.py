"""Generated from Smithy shape ``com.amazonaws.directoryservice#GetSnapshotLimitsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id


class GetSnapshotLimitsRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>Contains the identifier of the directory to obtain the limits for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSnapshotLimitsRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSnapshotLimitsRequest:
    out: GetSnapshotLimitsRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("GetSnapshotLimitsRequest.directory_id required")
    return out
