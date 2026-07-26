"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DeleteFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.status


class DeleteFlowResponse(TypedDict, closed=True):
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that was deleted.</p>"""
    status: NotRequired["capo_mediaconnect.types.status.Status"]
    """<p> The status of the flow when the <code>DeleteFlow</code> process begins.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFlowResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "status" in value:
        import capo_mediaconnect.types.status

        out["status"] = capo_mediaconnect.types.status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> DeleteFlowResponse:
    out: DeleteFlowResponse = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "status" in data:
        import capo_mediaconnect.types.status

        out["status"] = capo_mediaconnect.types.status.deserialize_json(data["status"])
    return out
