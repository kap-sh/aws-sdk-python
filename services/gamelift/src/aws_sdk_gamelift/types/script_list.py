"""Generated from Smithy shape ``com.amazonaws.gamelift#ScriptList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.script

ScriptList: TypeAlias = list["aws_sdk_gamelift.types.script.Script"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScriptList) -> list:
    import aws_sdk_gamelift.types.script

    out: list = []
    for item in value:
        out.append(aws_sdk_gamelift.types.script.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ScriptList:
    import aws_sdk_gamelift.types.script

    out: ScriptList = []
    for item in data:
        out.append(aws_sdk_gamelift.types.script.deserialize_aws_json_1_1(item))
    return out
