"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DeleteBrowserSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn

class DeleteBrowserSettingsRequest(TypedDict):
    browser_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the browser settings.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteBrowserSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBrowserSettingsRequest:
    out: DeleteBrowserSettingsRequest = {}  # type: ignore[typeddict-item]
    return out