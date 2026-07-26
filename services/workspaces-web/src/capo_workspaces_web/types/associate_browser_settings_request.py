"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateBrowserSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class AssociateBrowserSettingsRequest(TypedDict, closed=True):
    portal_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    browser_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the browser settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateBrowserSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssociateBrowserSettingsRequest:
    out: AssociateBrowserSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
