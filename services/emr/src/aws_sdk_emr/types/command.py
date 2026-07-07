"""Generated from Smithy shape ``com.amazonaws.emr#Command``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.string
    import aws_sdk_emr.types.string_list


class Command(TypedDict, closed=True):
    name: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The name of the command.</p>"""
    script_path: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The Amazon S3 location of the command script.</p>"""
    args: NotRequired["aws_sdk_emr.types.string_list.StringList"]
    """<p>Arguments for Amazon EMR to pass to the command for execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Command) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "script_path" in value:
        out["ScriptPath"] = value["script_path"]
    if "args" in value:
        import aws_sdk_emr.types.string_list

        out["Args"] = aws_sdk_emr.types.string_list.serialize_aws_json_1_1(
            value["args"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Command:
    out: Command = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ScriptPath" in data:
        out["script_path"] = data["ScriptPath"]
    if "Args" in data:
        import aws_sdk_emr.types.string_list

        out["args"] = aws_sdk_emr.types.string_list.deserialize_aws_json_1_1(
            data["Args"]
        )
    return out
