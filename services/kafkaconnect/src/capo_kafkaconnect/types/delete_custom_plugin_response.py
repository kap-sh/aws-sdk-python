"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#DeleteCustomPluginResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.custom_plugin_state


class DeleteCustomPluginResponse(TypedDict, closed=True):
    custom_plugin_arn: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the custom plugin that you requested to delete.</p>"""
    custom_plugin_state: NotRequired[
        "capo_kafkaconnect.types.custom_plugin_state.CustomPluginState"
    ]
    """<p>The state of the custom plugin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomPluginResponse) -> dict:
    out: dict = {}
    if "custom_plugin_arn" in value:
        out["customPluginArn"] = value["custom_plugin_arn"]
    if "custom_plugin_state" in value:
        out["customPluginState"] = value["custom_plugin_state"]
    return out


def deserialize_json(data: dict) -> DeleteCustomPluginResponse:
    out: DeleteCustomPluginResponse = {}  # type: ignore[typeddict-item]
    if "customPluginArn" in data:
        out["custom_plugin_arn"] = data["customPluginArn"]
    if "customPluginState" in data:
        out["custom_plugin_state"] = data["customPluginState"]
    return out
