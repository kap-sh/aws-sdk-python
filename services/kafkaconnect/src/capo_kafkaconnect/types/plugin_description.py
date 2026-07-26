"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#PluginDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.custom_plugin_description


class PluginDescription(TypedDict, closed=True):
    custom_plugin: NotRequired[
        "capo_kafkaconnect.types.custom_plugin_description.CustomPluginDescription"
    ]
    """<p>Details about a custom plugin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PluginDescription) -> dict:
    out: dict = {}
    if "custom_plugin" in value:
        import capo_kafkaconnect.types.custom_plugin_description

        out["customPlugin"] = (
            capo_kafkaconnect.types.custom_plugin_description.serialize_json(
                value["custom_plugin"]
            )
        )
    return out


def deserialize_json(data: dict) -> PluginDescription:
    out: PluginDescription = {}  # type: ignore[typeddict-item]
    if "customPlugin" in data:
        import capo_kafkaconnect.types.custom_plugin_description

        out["custom_plugin"] = (
            capo_kafkaconnect.types.custom_plugin_description.deserialize_json(
                data["customPlugin"]
            )
        )
    return out
