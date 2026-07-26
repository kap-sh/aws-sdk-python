"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetPluginRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.plugin_id


class GetPluginRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application which contains the plugin.</p>"""
    plugin_id: "capo_qbusiness.types.plugin_id.PluginId"
    """<p>The identifier of the plugin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPluginRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPluginRequest:
    out: GetPluginRequest = {}  # type: ignore[typeddict-item]
    return out
