"""Generated from Smithy shape ``com.amazonaws.directoryservice#ShareDirectoryResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id


class ShareDirectoryResult(TypedDict):
    shared_directory_id: NotRequired[
        "aws_sdk_directory_service.types.directory_id.DirectoryId"
    ]
    """<p>Identifier of the directory that is stored in the directory consumer account that is shared from the specified directory (<code>DirectoryId</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShareDirectoryResult) -> dict:
    out: dict = {}
    if "shared_directory_id" in value:
        out["SharedDirectoryId"] = value["shared_directory_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ShareDirectoryResult:
    out: ShareDirectoryResult = {}  # type: ignore[typeddict-item]
    if "SharedDirectoryId" in data:
        out["shared_directory_id"] = data["SharedDirectoryId"]
    return out
