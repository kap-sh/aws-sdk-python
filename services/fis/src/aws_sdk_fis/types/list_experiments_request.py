"""Generated from Smithy shape ``com.amazonaws.fis#ListExperimentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_template_id
    import aws_sdk_fis.types.list_experiments_max_results
    import aws_sdk_fis.types.next_token


class ListExperimentsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "aws_sdk_fis.types.list_experiments_max_results.ListExperimentsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_fis.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    experiment_template_id: NotRequired[
        "aws_sdk_fis.types.experiment_template_id.ExperimentTemplateId"
    ]
    """<p>The ID of the experiment template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExperimentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListExperimentsRequest:
    out: ListExperimentsRequest = {}  # type: ignore[typeddict-item]
    return out
