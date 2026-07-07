"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#Plugin``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kafkaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.custom_plugin


class Plugin(TypedDict, closed=True):
    custom_plugin: "aws_sdk_kafkaconnect.types.custom_plugin.CustomPlugin"
    """<p>Details about a custom plugin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Plugin) -> dict:
    out: dict = {}
    import aws_sdk_kafkaconnect.types.custom_plugin

    out["customPlugin"] = aws_sdk_kafkaconnect.types.custom_plugin.serialize_json(
        value["custom_plugin"]
    )
    return out


def deserialize_json(data: dict) -> Plugin:
    out: Plugin = {}  # type: ignore[typeddict-item]
    if "customPlugin" in data:
        import aws_sdk_kafkaconnect.types.custom_plugin

        out["custom_plugin"] = (
            aws_sdk_kafkaconnect.types.custom_plugin.deserialize_json(
                data["customPlugin"]
            )
        )
    else:
        raise DeserializationError("Plugin.custom_plugin required")
    return out
