"""Generated from Smithy shape ``com.amazonaws.emr#CommandList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.command

CommandList: TypeAlias = list["capo_emr.types.command.Command"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommandList) -> list:
    import capo_emr.types.command

    out: list = []
    for item in value:
        out.append(capo_emr.types.command.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CommandList:
    import capo_emr.types.command

    out: CommandList = []
    for item in data:
        out.append(capo_emr.types.command.deserialize_aws_json_1_1(item))
    return out
