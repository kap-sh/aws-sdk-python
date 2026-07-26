"""Generated from Smithy shape ``com.amazonaws.quicksight#GetFlowPermissionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.account_id
    import capo_quicksight.types.flow_id


class GetFlowPermissionsInput(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.account_id.AccountId"
    """<p>The ID of the Amazon Web Services account that contains the flow that you are getting permissions for.</p>"""
    flow_id: "capo_quicksight.types.flow_id.FlowId"
    """<p>The unique identifier of the flow to get permissions from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFlowPermissionsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFlowPermissionsInput:
    out: GetFlowPermissionsInput = {}  # type: ignore[typeddict-item]
    return out
