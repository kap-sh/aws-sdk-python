"""Generated from Smithy shape ``com.amazonaws.emr#ScriptBootstrapActionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.xml_string
    import capo_emr.types.xml_string_list


class ScriptBootstrapActionConfig(TypedDict, closed=True):
    path: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>Location in Amazon S3 of the script to run during a bootstrap action.</p>"""
    args: NotRequired["capo_emr.types.xml_string_list.XmlStringList"]
    """<p>A list of command line arguments to pass to the bootstrap action script.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScriptBootstrapActionConfig) -> dict:
    out: dict = {}
    if "path" in value:
        out["Path"] = value["path"]
    if "args" in value:
        import capo_emr.types.xml_string_list

        out["Args"] = capo_emr.types.xml_string_list.serialize_aws_json_1_1(
            value["args"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScriptBootstrapActionConfig:
    out: ScriptBootstrapActionConfig = {}  # type: ignore[typeddict-item]
    if "Path" in data:
        out["path"] = data["Path"]
    if "Args" in data:
        import capo_emr.types.xml_string_list

        out["args"] = capo_emr.types.xml_string_list.deserialize_aws_json_1_1(
            data["Args"]
        )
    return out
