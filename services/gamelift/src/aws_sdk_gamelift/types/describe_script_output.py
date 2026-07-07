"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeScriptOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.script


class DescribeScriptOutput(TypedDict, closed=True):
    script: NotRequired["aws_sdk_gamelift.types.script.Script"]
    """<p>A set of properties describing the requested script.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeScriptOutput) -> dict:
    out: dict = {}
    if "script" in value:
        import aws_sdk_gamelift.types.script

        out["Script"] = aws_sdk_gamelift.types.script.serialize_aws_json_1_1(
            value["script"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeScriptOutput:
    out: DescribeScriptOutput = {}  # type: ignore[typeddict-item]
    if "Script" in data:
        import aws_sdk_gamelift.types.script

        out["script"] = aws_sdk_gamelift.types.script.deserialize_aws_json_1_1(
            data["Script"]
        )
    return out
