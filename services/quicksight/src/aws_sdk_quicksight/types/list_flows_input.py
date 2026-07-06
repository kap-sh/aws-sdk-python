"""Generated from Smithy shape ``com.amazonaws.quicksight#ListFlowsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.account_id
    import aws_sdk_quicksight.types.flow_max_results


class ListFlowsInput(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.account_id.AccountId"
    """<p>The ID of the Amazon Web Services account that contains the flow list that you are getting.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to request the next set of results, or null if you want to retrieve the first set.</p>"""
    max_results: NotRequired["aws_sdk_quicksight.types.flow_max_results.FlowMaxResults"]
    """<p>The maximum number of results to be returned per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFlowsInput:
    out: ListFlowsInput = {}  # type: ignore[typeddict-item]
    return out
