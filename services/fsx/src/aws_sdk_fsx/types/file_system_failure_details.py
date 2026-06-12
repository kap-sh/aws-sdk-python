"""Generated from Smithy shape ``com.amazonaws.fsx#FileSystemFailureDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.error_message


class FileSystemFailureDetails(TypedDict):
    message: NotRequired["aws_sdk_fsx.types.error_message.ErrorMessage"]
    """<p>A message describing any failures that occurred.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemFailureDetails) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FileSystemFailureDetails:
    out: FileSystemFailureDetails = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
