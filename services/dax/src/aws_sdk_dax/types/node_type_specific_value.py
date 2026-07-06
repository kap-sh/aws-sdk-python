"""Generated from Smithy shape ``com.amazonaws.dax#NodeTypeSpecificValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dax.types.string


class NodeTypeSpecificValue(TypedDict, closed=True):
    node_type: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>A node type to which the parameter value applies.</p>"""
    value: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>The parameter value for this node type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeTypeSpecificValue) -> dict:
    out: dict = {}
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NodeTypeSpecificValue:
    out: NodeTypeSpecificValue = {}  # type: ignore[typeddict-item]
    if "NodeType" in data:
        out["node_type"] = data["NodeType"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
