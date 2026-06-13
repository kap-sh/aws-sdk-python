"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetPluginRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.plugin_id


class GetPluginRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application which contains the plugin.</p>"""
    plugin_id: "aws_sdk_qbusiness.types.plugin_id.PluginId"
    """<p>The identifier of the plugin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPluginRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPluginRequest:
    out: GetPluginRequest = {}  # type: ignore[typeddict-item]
    return out
