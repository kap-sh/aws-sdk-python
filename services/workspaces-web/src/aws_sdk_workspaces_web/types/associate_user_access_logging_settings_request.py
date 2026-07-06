"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateUserAccessLoggingSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class AssociateUserAccessLoggingSettingsRequest(TypedDict, closed=True):
    portal_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    user_access_logging_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the user access logging settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateUserAccessLoggingSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssociateUserAccessLoggingSettingsRequest:
    out: AssociateUserAccessLoggingSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
