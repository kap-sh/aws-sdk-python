"""Generated from Smithy shape ``com.amazonaws.fsx#FileCacheFailureDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.error_message


class FileCacheFailureDetails(TypedDict, closed=True):
    message: NotRequired["aws_sdk_fsx.types.error_message.ErrorMessage"]
    """<p>A message describing any failures that occurred.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileCacheFailureDetails) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FileCacheFailureDetails:
    out: FileCacheFailureDetails = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
