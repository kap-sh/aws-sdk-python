"""Generated from Smithy shape ``com.amazonaws.kafka#ListConfigurationRevisionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.max_results


class ListConfigurationRevisionsRequest(TypedDict, closed=True):
    arn: "capo_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.</p>"""
    max_results: NotRequired["capo_kafka.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.</p>"""
    next_token: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationRevisionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListConfigurationRevisionsRequest:
    out: ListConfigurationRevisionsRequest = {}  # type: ignore[typeddict-item]
    return out
