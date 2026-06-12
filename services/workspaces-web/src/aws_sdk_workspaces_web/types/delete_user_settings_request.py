"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DeleteUserSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn

class DeleteUserSettingsRequest(TypedDict):
    user_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the user settings.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteUserSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteUserSettingsRequest:
    out: DeleteUserSettingsRequest = {}  # type: ignore[typeddict-item]
    return out