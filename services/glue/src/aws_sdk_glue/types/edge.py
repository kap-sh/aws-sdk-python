"""Generated from Smithy shape ``com.amazonaws.glue#Edge``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string


class Edge(TypedDict):
    source_id: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The unique of the node within the workflow where the edge starts.</p>"""
    destination_id: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The unique of the node within the workflow where the edge ends.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Edge) -> dict:
    out: dict = {}
    if "source_id" in value:
        out["SourceId"] = value["source_id"]
    if "destination_id" in value:
        out["DestinationId"] = value["destination_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Edge:
    out: Edge = {}  # type: ignore[typeddict-item]
    if "SourceId" in data:
        out["source_id"] = data["SourceId"]
    if "DestinationId" in data:
        out["destination_id"] = data["DestinationId"]
    return out
