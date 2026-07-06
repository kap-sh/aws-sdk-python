"""Generated from Smithy shape ``com.amazonaws.quicksight#ListIngestionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.ingestion_max_results
    import aws_sdk_quicksight.types.string


class ListIngestionsRequest(TypedDict, closed=True):
    data_set_id: "aws_sdk_quicksight.types.string.String"
    """<p>The ID of the dataset used in the ingestion.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    max_results: NotRequired[
        "aws_sdk_quicksight.types.ingestion_max_results.IngestionMaxResults"
    ]
    """<p>The maximum number of results to be returned per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIngestionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIngestionsRequest:
    out: ListIngestionsRequest = {}  # type: ignore[typeddict-item]
    return out
