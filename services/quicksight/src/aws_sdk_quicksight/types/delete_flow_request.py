"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteFlowRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.account_id
    import aws_sdk_quicksight.types.flow_id


class DeleteFlowRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.account_id.AccountId"
    """<p>The ID of the Amazon Web Services account that contains the flow that you are deleting.</p>"""
    flow_id: "aws_sdk_quicksight.types.flow_id.FlowId"
    """<p>The unique identifier of the flow to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFlowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFlowRequest:
    out: DeleteFlowRequest = {}  # type: ignore[typeddict-item]
    return out
