"""Generated from Smithy shape ``com.amazonaws.qbusiness#DeletePluginRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.plugin_id

class DeletePluginRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier the application attached to the Amazon Q Business plugin.</p>"""
    plugin_id: "aws_sdk_qbusiness.types.plugin_id.PluginId"
    """<p>The identifier of the plugin being deleted.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeletePluginRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePluginRequest:
    out: DeletePluginRequest = {}  # type: ignore[typeddict-item]
    return out