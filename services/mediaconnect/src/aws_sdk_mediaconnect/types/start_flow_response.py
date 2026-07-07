"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StartFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.status


class StartFlowResponse(TypedDict, closed=True):
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that you started.</p>"""
    status: NotRequired["aws_sdk_mediaconnect.types.status.Status"]
    """<p> The status of the flow when the <code>StartFlow</code> process begins.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartFlowResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "status" in value:
        import aws_sdk_mediaconnect.types.status

        out["status"] = aws_sdk_mediaconnect.types.status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> StartFlowResponse:
    out: StartFlowResponse = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "status" in data:
        import aws_sdk_mediaconnect.types.status

        out["status"] = aws_sdk_mediaconnect.types.status.deserialize_json(
            data["status"]
        )
    return out
