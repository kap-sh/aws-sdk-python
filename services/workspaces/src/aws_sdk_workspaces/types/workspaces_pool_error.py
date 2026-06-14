"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesPoolError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.error_message
    import aws_sdk_workspaces.types.workspaces_pool_error_code


class WorkspacesPoolError(TypedDict):
    error_code: NotRequired[
        "aws_sdk_workspaces.types.workspaces_pool_error_code.WorkspacesPoolErrorCode"
    ]
    """<p>The error code.</p>"""
    error_message: NotRequired["aws_sdk_workspaces.types.error_message.ErrorMessage"]
    """<p>The error message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesPoolError) -> dict:
    out: dict = {}
    if "error_code" in value:
        import aws_sdk_workspaces.types.workspaces_pool_error_code

        out["ErrorCode"] = (
            aws_sdk_workspaces.types.workspaces_pool_error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspacesPoolError:
    out: WorkspacesPoolError = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        import aws_sdk_workspaces.types.workspaces_pool_error_code

        out["error_code"] = (
            aws_sdk_workspaces.types.workspaces_pool_error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
