"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateUserSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class AssociateUserSettingsRequest(TypedDict):
    portal_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    user_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the user settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateUserSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssociateUserSettingsRequest:
    out: AssociateUserSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
