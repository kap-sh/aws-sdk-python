"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.account_id
    import capo_quicksight.types.flow_id
    import capo_quicksight.types.flow_publish_state


class DescribeFlowRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.account_id.AccountId"
    """<p>The ID of the Amazon Web Services account that contains the flow that you are describing.</p>"""
    flow_id: "capo_quicksight.types.flow_id.FlowId"
    """<p>The unique identifier of the flow.</p>"""
    publish_state: "capo_quicksight.types.flow_publish_state.FlowPublishState"
    """<p>The publish state of the flow version to describe. Valid values are <code>DRAFT</code>, <code>PUBLISHED</code>, or <code>PENDING_APPROVAL</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFlowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeFlowRequest:
    out: DescribeFlowRequest = {}  # type: ignore[typeddict-item]
    return out
