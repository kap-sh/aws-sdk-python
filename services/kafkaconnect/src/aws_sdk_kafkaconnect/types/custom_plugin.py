"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#CustomPlugin``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kafkaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__long_min1
    import aws_sdk_kafkaconnect.types.__string


class CustomPlugin(TypedDict):
    custom_plugin_arn: "aws_sdk_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the custom plugin.</p>"""
    revision: "aws_sdk_kafkaconnect.types.__long_min1.__longMin1"
    """<p>The revision of the custom plugin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomPlugin) -> dict:
    out: dict = {}
    out["customPluginArn"] = value["custom_plugin_arn"]
    out["revision"] = value.get("revision", 0)
    return out


def deserialize_json(data: dict) -> CustomPlugin:
    out: CustomPlugin = {}  # type: ignore[typeddict-item]
    if "customPluginArn" in data:
        out["custom_plugin_arn"] = data["customPluginArn"]
    else:
        raise DeserializationError("CustomPlugin.custom_plugin_arn required")
    if "revision" in data:
        out["revision"] = data["revision"]
    else:
        out["revision"] = 0
    return out
