"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#PluginDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.custom_plugin_description


class PluginDescription(TypedDict):
    custom_plugin: NotRequired[
        "aws_sdk_kafkaconnect.types.custom_plugin_description.CustomPluginDescription"
    ]
    """<p>Details about a custom plugin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PluginDescription) -> dict:
    out: dict = {}
    if "custom_plugin" in value:
        import aws_sdk_kafkaconnect.types.custom_plugin_description

        out["customPlugin"] = (
            aws_sdk_kafkaconnect.types.custom_plugin_description.serialize_json(
                value["custom_plugin"]
            )
        )
    return out


def deserialize_json(data: dict) -> PluginDescription:
    out: PluginDescription = {}  # type: ignore[typeddict-item]
    if "customPlugin" in data:
        import aws_sdk_kafkaconnect.types.custom_plugin_description

        out["custom_plugin"] = (
            aws_sdk_kafkaconnect.types.custom_plugin_description.deserialize_json(
                data["customPlugin"]
            )
        )
    return out
