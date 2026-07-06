"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateMicrosoftADResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id


class CreateMicrosoftADResult(TypedDict, closed=True):
    directory_id: NotRequired[
        "aws_sdk_directory_service.types.directory_id.DirectoryId"
    ]
    """<p>The identifier of the directory that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMicrosoftADResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMicrosoftADResult:
    out: CreateMicrosoftADResult = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    return out
