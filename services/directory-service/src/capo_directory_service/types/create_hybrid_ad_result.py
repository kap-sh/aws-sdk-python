"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateHybridADResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id


class CreateHybridADResult(TypedDict, closed=True):
    directory_id: NotRequired["capo_directory_service.types.directory_id.DirectoryId"]
    """<p>The unique identifier of the newly created hybrid directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHybridADResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHybridADResult:
    out: CreateHybridADResult = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    return out
