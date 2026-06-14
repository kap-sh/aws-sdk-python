"""Generated from Smithy shape ``com.amazonaws.workspaces#ErrorDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.description
    import aws_sdk_workspaces.types.workspace_image_error_detail_code


class ErrorDetails(TypedDict):
    error_code: NotRequired[
        "aws_sdk_workspaces.types.workspace_image_error_detail_code.WorkspaceImageErrorDetailCode"
    ]
    """<p>Indicates the error code returned.</p>"""
    error_message: NotRequired["aws_sdk_workspaces.types.description.Description"]
    """<p>The text of the error message related the error code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorDetails) -> dict:
    out: dict = {}
    if "error_code" in value:
        import aws_sdk_workspaces.types.workspace_image_error_detail_code

        out["ErrorCode"] = (
            aws_sdk_workspaces.types.workspace_image_error_detail_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ErrorDetails:
    out: ErrorDetails = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        import aws_sdk_workspaces.types.workspace_image_error_detail_code

        out["error_code"] = (
            aws_sdk_workspaces.types.workspace_image_error_detail_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
