"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RemoveFlowSourceResponse``."""

from typing import TypedDict

from typing_extensions import NotRequired


class RemoveFlowSourceResponse(TypedDict):
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that the source was removed from. </p>"""
    source_arn: NotRequired["str"]
    """<p> The ARN of the source that was removed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveFlowSourceResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "source_arn" in value:
        out["sourceArn"] = value["source_arn"]
    return out


def deserialize_json(data: dict) -> RemoveFlowSourceResponse:
    out: RemoveFlowSourceResponse = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "sourceArn" in data:
        out["source_arn"] = data["sourceArn"]
    return out
