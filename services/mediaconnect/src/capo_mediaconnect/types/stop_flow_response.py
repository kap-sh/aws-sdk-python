"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StopFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.status


class StopFlowResponse(TypedDict, closed=True):
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that you stopped.</p>"""
    status: NotRequired["capo_mediaconnect.types.status.Status"]
    """<p> The status of the flow when the <code>StopFlow</code> process begins.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopFlowResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "status" in value:
        import capo_mediaconnect.types.status

        out["status"] = capo_mediaconnect.types.status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> StopFlowResponse:
    out: StopFlowResponse = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "status" in data:
        import capo_mediaconnect.types.status

        out["status"] = capo_mediaconnect.types.status.deserialize_json(data["status"])
    return out
