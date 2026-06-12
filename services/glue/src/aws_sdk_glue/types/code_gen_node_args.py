"""Generated from Smithy shape ``com.amazonaws.glue#CodeGenNodeArgs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.code_gen_node_arg

CodeGenNodeArgs: TypeAlias = list["aws_sdk_glue.types.code_gen_node_arg.CodeGenNodeArg"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeGenNodeArgs) -> list:
    import aws_sdk_glue.types.code_gen_node_arg

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.code_gen_node_arg.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CodeGenNodeArgs:
    import aws_sdk_glue.types.code_gen_node_arg

    out: CodeGenNodeArgs = []
    for item in data:
        out.append(aws_sdk_glue.types.code_gen_node_arg.deserialize_aws_json_1_1(item))
    return out
