"""Generated from Smithy shape ``com.amazonaws.directoryservice#RejectSharedDirectoryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id


class RejectSharedDirectoryResult(TypedDict, closed=True):
    shared_directory_id: NotRequired[
        "aws_sdk_directory_service.types.directory_id.DirectoryId"
    ]
    """<p>Identifier of the shared directory in the directory consumer account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RejectSharedDirectoryResult) -> dict:
    out: dict = {}
    if "shared_directory_id" in value:
        out["SharedDirectoryId"] = value["shared_directory_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RejectSharedDirectoryResult:
    out: RejectSharedDirectoryResult = {}  # type: ignore[typeddict-item]
    if "SharedDirectoryId" in data:
        out["shared_directory_id"] = data["SharedDirectoryId"]
    return out
