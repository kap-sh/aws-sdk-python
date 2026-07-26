"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetBrowserSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class GetBrowserSettingsRequest(TypedDict, closed=True):
    browser_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the browser settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBrowserSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBrowserSettingsRequest:
    out: GetBrowserSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
