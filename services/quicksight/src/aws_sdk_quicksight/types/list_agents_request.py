"""Generated from Smithy shape ``com.amazonaws.quicksight#ListAgentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.list_agents_request_max_results_integer


class ListAgentsRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the agents.</p>"""
    max_results: NotRequired[
        "aws_sdk_quicksight.types.list_agents_request_max_results_integer.ListAgentsRequestMaxResultsInteger"
    ]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAgentsRequest:
    out: ListAgentsRequest = {}  # type: ignore[typeddict-item]
    return out
