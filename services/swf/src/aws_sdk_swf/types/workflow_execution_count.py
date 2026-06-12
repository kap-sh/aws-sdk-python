"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionCount``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_swf.types.count
    import aws_sdk_swf.types.truncated


class WorkflowExecutionCount(TypedDict):
    count: "aws_sdk_swf.types.count.Count"
    """<p>The number of workflow executions.</p>"""
    truncated: "aws_sdk_swf.types.truncated.Truncated"
    """<p>If set to true, indicates that the actual count was more than the maximum supported by this API and the count returned is the truncated value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecutionCount) -> dict:
    out: dict = {}
    out["count"] = value.get("count", 0)
    out["truncated"] = value.get("truncated", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowExecutionCount:
    out: WorkflowExecutionCount = {}  # type: ignore[typeddict-item]
    if "count" in data:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    if "truncated" in data:
        out["truncated"] = data["truncated"]
    else:
        out["truncated"] = False
    return out
