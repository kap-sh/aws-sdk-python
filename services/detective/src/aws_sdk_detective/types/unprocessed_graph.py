"""Generated from Smithy shape ``com.amazonaws.detective#UnprocessedGraph``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_detective.types.graph_arn
    import aws_sdk_detective.types.unprocessed_reason


class UnprocessedGraph(TypedDict, closed=True):
    graph_arn: NotRequired["aws_sdk_detective.types.graph_arn.GraphArn"]
    """<p>The ARN of the organization behavior graph.</p>"""
    reason: NotRequired["aws_sdk_detective.types.unprocessed_reason.UnprocessedReason"]
    """<p>The reason data source package information could not be processed for a behavior graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedGraph) -> dict:
    out: dict = {}
    if "graph_arn" in value:
        out["GraphArn"] = value["graph_arn"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> UnprocessedGraph:
    out: UnprocessedGraph = {}  # type: ignore[typeddict-item]
    if "GraphArn" in data:
        out["graph_arn"] = data["GraphArn"]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    return out
