"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchGetCommitsError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.error_code
    import aws_sdk_codecommit.types.error_message
    import aws_sdk_codecommit.types.object_id


class BatchGetCommitsError(TypedDict):
    commit_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>A commit ID that either could not be found or was not in a valid format.</p>"""
    error_code: NotRequired["aws_sdk_codecommit.types.error_code.ErrorCode"]
    """<p>An error code that specifies whether the commit ID was not valid or not found.</p>"""
    error_message: NotRequired["aws_sdk_codecommit.types.error_message.ErrorMessage"]
    """<p>An error message that provides detail about why the commit ID either was not found or was not valid.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetCommitsError) -> dict:
    out: dict = {}
    if "commit_id" in value:
        out["commitId"] = value["commit_id"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetCommitsError:
    out: BatchGetCommitsError = {}  # type: ignore[typeddict-item]
    if "commitId" in data:
        out["commit_id"] = data["commitId"]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
