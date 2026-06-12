"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DeleteUserAccessLoggingSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn

class DeleteUserAccessLoggingSettingsRequest(TypedDict):
    user_access_logging_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the user access logging settings.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteUserAccessLoggingSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteUserAccessLoggingSettingsRequest:
    out: DeleteUserAccessLoggingSettingsRequest = {}  # type: ignore[typeddict-item]
    return out