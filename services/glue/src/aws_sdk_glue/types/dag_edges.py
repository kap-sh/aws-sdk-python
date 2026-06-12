"""Generated from Smithy shape ``com.amazonaws.glue#DagEdges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.code_gen_edge

DagEdges: TypeAlias = list["aws_sdk_glue.types.code_gen_edge.CodeGenEdge"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DagEdges) -> list:
    import aws_sdk_glue.types.code_gen_edge

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.code_gen_edge.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DagEdges:
    import aws_sdk_glue.types.code_gen_edge

    out: DagEdges = []
    for item in data:
        out.append(aws_sdk_glue.types.code_gen_edge.deserialize_aws_json_1_1(item))
    return out
