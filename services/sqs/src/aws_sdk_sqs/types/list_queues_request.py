"""Generated from Smithy shape ``com.amazonaws.sqs#ListQueuesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sqs.types.boxed_integer
    import aws_sdk_sqs.types.string
    import aws_sdk_sqs.types.token


class ListQueuesRequest(TypedDict, closed=True):
    queue_name_prefix: NotRequired["aws_sdk_sqs.types.string.String"]
    """<p>A string to use for filtering the list results. Only those queues whose name begins with the specified string are returned.</p> <p>Queue URLs and names are case-sensitive.</p>"""
    next_token: NotRequired["aws_sdk_sqs.types.token.Token"]
    """<p>Pagination token to request the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_sqs.types.boxed_integer.BoxedInteger"]
    """<p>Maximum number of results to include in the response. Value range is 1 to 1000. You must set <code>MaxResults</code> to receive a value for <code>NextToken</code> in the response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListQueuesRequest) -> dict:
    out: dict = {}
    if "queue_name_prefix" in value:
        out["QueueNamePrefix"] = value["queue_name_prefix"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListQueuesRequest:
    out: ListQueuesRequest = {}  # type: ignore[typeddict-item]
    if "QueueNamePrefix" in data:
        out["queue_name_prefix"] = data["QueueNamePrefix"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
