"""Generated from Smithy shape ``com.amazonaws.workspaces#CustomWorkspaceImageImportErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.error_code
    import aws_sdk_workspaces.types.image_error_message


class CustomWorkspaceImageImportErrorDetails(TypedDict, closed=True):
    error_code: NotRequired["aws_sdk_workspaces.types.error_code.ErrorCode"]
    """<p>The error code that is returned for the image import.</p>"""
    error_message: NotRequired[
        "aws_sdk_workspaces.types.image_error_message.ImageErrorMessage"
    ]
    """<p>The text of the error message that is returned for the image import.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomWorkspaceImageImportErrorDetails) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomWorkspaceImageImportErrorDetails:
    out: CustomWorkspaceImageImportErrorDetails = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
