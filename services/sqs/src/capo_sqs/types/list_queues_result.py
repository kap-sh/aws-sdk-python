"""Generated from Smithy shape ``com.amazonaws.sqs#ListQueuesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.queue_url_list
    import capo_sqs.types.token


class ListQueuesResult(TypedDict, closed=True):
    queue_urls: NotRequired["capo_sqs.types.queue_url_list.QueueUrlList"]
    """<p>A list of queue URLs, up to 1,000 entries, or the value of <code>MaxResults</code> that you sent in the request.</p>"""
    next_token: NotRequired["capo_sqs.types.token.Token"]
    """<p>Pagination token to include in the next request. Token value is <code>null</code> if there are no additional results to request, or if you did not set <code>MaxResults</code> in the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListQueuesResult) -> dict:
    out: dict = {}
    if "queue_urls" in value:
        import capo_sqs.types.queue_url_list

        out["QueueUrls"] = capo_sqs.types.queue_url_list.serialize_aws_json_1_0(
            value["queue_urls"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListQueuesResult:
    out: ListQueuesResult = {}  # type: ignore[typeddict-item]
    if data.get("QueueUrls") is not None:
        import capo_sqs.types.queue_url_list

        out["queue_urls"] = capo_sqs.types.queue_url_list.deserialize_aws_json_1_0(
            data["QueueUrls"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
