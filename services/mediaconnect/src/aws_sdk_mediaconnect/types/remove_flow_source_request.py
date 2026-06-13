"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RemoveFlowSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.flow_arn


class RemoveFlowSourceRequest(TypedDict):
    flow_arn: "aws_sdk_mediaconnect.types.flow_arn.FlowArn"
    """<p> The Amazon Resource Name (ARN) of the flow that you want to remove a source from.</p>"""
    source_arn: "str"
    """<p> The ARN of the source that you want to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveFlowSourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveFlowSourceRequest:
    out: RemoveFlowSourceRequest = {}  # type: ignore[typeddict-item]
    return out
