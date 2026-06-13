"""Generated from Smithy shape ``com.amazonaws.quicksight#ListActionConnectorsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.max_results


class ListActionConnectorsRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID for which to list action connectors.</p>"""
    max_results: NotRequired["aws_sdk_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of action connectors to return in a single response. Valid range is 1 to 100.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token to retrieve the next set of results. Use the token returned from a previous call to continue listing action connectors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListActionConnectorsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListActionConnectorsRequest:
    out: ListActionConnectorsRequest = {}  # type: ignore[typeddict-item]
    return out
