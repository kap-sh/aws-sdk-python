"""Generated from Smithy shape ``com.amazonaws.sqs#ListDeadLetterSourceQueuesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sqs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.queue_url_list
    import aws_sdk_sqs.types.token


class ListDeadLetterSourceQueuesResult(TypedDict):
    queue_urls: "aws_sdk_sqs.types.queue_url_list.QueueUrlList"
    """<p>A list of source queue URLs that have the <code>RedrivePolicy</code> queue attribute configured with a dead-letter queue.</p>"""
    next_token: NotRequired["aws_sdk_sqs.types.token.Token"]
    """<p>Pagination token to include in the next request. Token value is <code>null</code> if there are no additional results to request, or if you did not set <code>MaxResults</code> in the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDeadLetterSourceQueuesResult) -> dict:
    out: dict = {}
    import aws_sdk_sqs.types.queue_url_list

    out["queueUrls"] = aws_sdk_sqs.types.queue_url_list.serialize_aws_json_1_0(
        value["queue_urls"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDeadLetterSourceQueuesResult:
    out: ListDeadLetterSourceQueuesResult = {}  # type: ignore[typeddict-item]
    if "queueUrls" in data:
        import aws_sdk_sqs.types.queue_url_list

        out["queue_urls"] = aws_sdk_sqs.types.queue_url_list.deserialize_aws_json_1_0(
            data["queueUrls"]
        )
    else:
        raise DeserializationError(
            "ListDeadLetterSourceQueuesResult.queue_urls required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
