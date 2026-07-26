"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DeleteUserSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class DeleteUserSettingsRequest(TypedDict, closed=True):
    user_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the user settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUserSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteUserSettingsRequest:
    out: DeleteUserSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
