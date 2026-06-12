"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#CreateCustomPluginResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__long
    import aws_sdk_kafkaconnect.types.__string
    import aws_sdk_kafkaconnect.types.custom_plugin_state


class CreateCustomPluginResponse(TypedDict):
    custom_plugin_arn: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) that Amazon assigned to the custom plugin.</p>"""
    custom_plugin_state: NotRequired[
        "aws_sdk_kafkaconnect.types.custom_plugin_state.CustomPluginState"
    ]
    """<p>The state of the custom plugin.</p>"""
    name: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The name of the custom plugin.</p>"""
    revision: "aws_sdk_kafkaconnect.types.__long.__long"
    """<p>The revision of the custom plugin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomPluginResponse) -> dict:
    out: dict = {}
    if "custom_plugin_arn" in value:
        out["customPluginArn"] = value["custom_plugin_arn"]
    if "custom_plugin_state" in value:
        out["customPluginState"] = value["custom_plugin_state"]
    if "name" in value:
        out["name"] = value["name"]
    out["revision"] = value.get("revision", 0)
    return out


def deserialize_json(data: dict) -> CreateCustomPluginResponse:
    out: CreateCustomPluginResponse = {}  # type: ignore[typeddict-item]
    if "customPluginArn" in data:
        out["custom_plugin_arn"] = data["customPluginArn"]
    if "customPluginState" in data:
        out["custom_plugin_state"] = data["customPluginState"]
    if "name" in data:
        out["name"] = data["name"]
    if "revision" in data:
        out["revision"] = data["revision"]
    else:
        out["revision"] = 0
    return out
