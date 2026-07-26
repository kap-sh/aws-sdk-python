"""Generated from Smithy shape ``com.amazonaws.glue#DagNodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.code_gen_node

DagNodes: TypeAlias = list["capo_glue.types.code_gen_node.CodeGenNode"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DagNodes) -> list:
    import capo_glue.types.code_gen_node

    out: list = []
    for item in value:
        out.append(capo_glue.types.code_gen_node.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DagNodes:
    import capo_glue.types.code_gen_node

    out: DagNodes = []
    for item in data:
        out.append(capo_glue.types.code_gen_node.deserialize_aws_json_1_1(item))
    return out
