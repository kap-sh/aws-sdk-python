"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DeleteFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.flow_arn


class DeleteFlowRequest(TypedDict, closed=True):
    flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn"
    """<p> The Amazon Resource Name (ARN) of the flow that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFlowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFlowRequest:
    out: DeleteFlowRequest = {}  # type: ignore[typeddict-item]
    return out
