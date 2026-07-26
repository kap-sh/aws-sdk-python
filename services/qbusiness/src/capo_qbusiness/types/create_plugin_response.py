"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreatePluginResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.plugin_arn
    import capo_qbusiness.types.plugin_build_status
    import capo_qbusiness.types.plugin_id


class CreatePluginResponse(TypedDict, closed=True):
    plugin_id: NotRequired["capo_qbusiness.types.plugin_id.PluginId"]
    """<p>The identifier of the plugin created.</p>"""
    plugin_arn: NotRequired["capo_qbusiness.types.plugin_arn.PluginArn"]
    """<p>The Amazon Resource Name (ARN) of a plugin.</p>"""
    build_status: NotRequired[
        "capo_qbusiness.types.plugin_build_status.PluginBuildStatus"
    ]
    """<p>The current status of a plugin. A plugin is modified asynchronously.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePluginResponse) -> dict:
    out: dict = {}
    if "plugin_id" in value:
        out["pluginId"] = value["plugin_id"]
    if "plugin_arn" in value:
        out["pluginArn"] = value["plugin_arn"]
    if "build_status" in value:
        import capo_qbusiness.types.plugin_build_status

        out["buildStatus"] = capo_qbusiness.types.plugin_build_status.serialize_json(
            value["build_status"]
        )
    return out


def deserialize_json(data: dict) -> CreatePluginResponse:
    out: CreatePluginResponse = {}  # type: ignore[typeddict-item]
    if "pluginId" in data:
        out["plugin_id"] = data["pluginId"]
    if "pluginArn" in data:
        out["plugin_arn"] = data["pluginArn"]
    if "buildStatus" in data:
        import capo_qbusiness.types.plugin_build_status

        out["build_status"] = capo_qbusiness.types.plugin_build_status.deserialize_json(
            data["buildStatus"]
        )
    return out
