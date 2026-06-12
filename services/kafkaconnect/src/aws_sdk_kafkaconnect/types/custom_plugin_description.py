"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#CustomPluginDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__long
    import aws_sdk_kafkaconnect.types.__string


class CustomPluginDescription(TypedDict):
    custom_plugin_arn: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the custom plugin.</p>"""
    revision: "aws_sdk_kafkaconnect.types.__long.__long"
    """<p>The revision of the custom plugin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomPluginDescription) -> dict:
    out: dict = {}
    if "custom_plugin_arn" in value:
        out["customPluginArn"] = value["custom_plugin_arn"]
    out["revision"] = value.get("revision", 0)
    return out


def deserialize_json(data: dict) -> CustomPluginDescription:
    out: CustomPluginDescription = {}  # type: ignore[typeddict-item]
    if "customPluginArn" in data:
        out["custom_plugin_arn"] = data["customPluginArn"]
    if "revision" in data:
        out["revision"] = data["revision"]
    else:
        out["revision"] = 0
    return out
