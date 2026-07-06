"""Generated from Smithy shape ``com.amazonaws.quicksight#ListSelfUpgradesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.max_results
    import aws_sdk_quicksight.types.namespace
    import aws_sdk_quicksight.types.string


class ListSelfUpgradesRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the self-upgrade requests.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The Quick namespace for the self-upgrade requests.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    max_results: NotRequired["aws_sdk_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSelfUpgradesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSelfUpgradesRequest:
    out: ListSelfUpgradesRequest = {}  # type: ignore[typeddict-item]
    return out
