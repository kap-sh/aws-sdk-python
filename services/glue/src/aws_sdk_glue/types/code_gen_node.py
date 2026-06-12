"""Generated from Smithy shape ``com.amazonaws.glue#CodeGenNode``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.code_gen_identifier
    import aws_sdk_glue.types.code_gen_node_args
    import aws_sdk_glue.types.code_gen_node_type
    import aws_sdk_glue.types.integer


class CodeGenNode(TypedDict):
    id: "aws_sdk_glue.types.code_gen_identifier.CodeGenIdentifier"
    """<p>A node identifier that is unique within the node's graph.</p>"""
    node_type: "aws_sdk_glue.types.code_gen_node_type.CodeGenNodeType"
    """<p>The type of node that this is.</p>"""
    args: "aws_sdk_glue.types.code_gen_node_args.CodeGenNodeArgs"
    """<p>Properties of the node, in the form of name-value pairs.</p>"""
    line_number: "aws_sdk_glue.types.integer.Integer"
    """<p>The line number of the node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeGenNode) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["NodeType"] = value["node_type"]
    import aws_sdk_glue.types.code_gen_node_args

    out["Args"] = aws_sdk_glue.types.code_gen_node_args.serialize_aws_json_1_1(
        value["args"]
    )
    out["LineNumber"] = value.get("line_number", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeGenNode:
    out: CodeGenNode = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("CodeGenNode.id required")
    if "NodeType" in data:
        out["node_type"] = data["NodeType"]
    else:
        raise DeserializationError("CodeGenNode.node_type required")
    if "Args" in data:
        import aws_sdk_glue.types.code_gen_node_args

        out["args"] = aws_sdk_glue.types.code_gen_node_args.deserialize_aws_json_1_1(
            data["Args"]
        )
    else:
        raise DeserializationError("CodeGenNode.args required")
    if "LineNumber" in data:
        out["line_number"] = data["LineNumber"]
    else:
        out["line_number"] = 0
    return out
