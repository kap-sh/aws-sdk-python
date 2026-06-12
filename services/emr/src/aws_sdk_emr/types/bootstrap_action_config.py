"""Generated from Smithy shape ``com.amazonaws.emr#BootstrapActionConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.script_bootstrap_action_config
    import aws_sdk_emr.types.xml_string_max_len256


class BootstrapActionConfig(TypedDict):
    name: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The name of the bootstrap action.</p>"""
    script_bootstrap_action: NotRequired[
        "aws_sdk_emr.types.script_bootstrap_action_config.ScriptBootstrapActionConfig"
    ]
    """<p>The script run by the bootstrap action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BootstrapActionConfig) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "script_bootstrap_action" in value:
        import aws_sdk_emr.types.script_bootstrap_action_config

        out["ScriptBootstrapAction"] = (
            aws_sdk_emr.types.script_bootstrap_action_config.serialize_aws_json_1_1(
                value["script_bootstrap_action"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BootstrapActionConfig:
    out: BootstrapActionConfig = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ScriptBootstrapAction" in data:
        import aws_sdk_emr.types.script_bootstrap_action_config

        out["script_bootstrap_action"] = (
            aws_sdk_emr.types.script_bootstrap_action_config.deserialize_aws_json_1_1(
                data["ScriptBootstrapAction"]
            )
        )
    return out
