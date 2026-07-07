"""Generated from Smithy shape ``com.amazonaws.sns#PublishBatchInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sns.types.publish_batch_request_entry_list
    import aws_sdk_sns.types.topic_arn


class PublishBatchInput(TypedDict, closed=True):
    topic_arn: "aws_sdk_sns.types.topic_arn.topicARN"
    """<p>The Amazon resource name (ARN) of the topic you want to batch publish to.</p>"""
    publish_batch_request_entries: "aws_sdk_sns.types.publish_batch_request_entry_list.PublishBatchRequestEntryList"
    """<p>A list of <code>PublishBatch</code> request entries to be sent to the SNS topic.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PublishBatchInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.TopicArn", str(value["topic_arn"])))
    import aws_sdk_sns.types.publish_batch_request_entry_list

    aws_sdk_sns.types.publish_batch_request_entry_list.serialize_query(
        value["publish_batch_request_entries"],
        pairs,
        f"{prefix}.PublishBatchRequestEntries",
    )


def deserialize_query(el: Element) -> PublishBatchInput:
    out: PublishBatchInput = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    else:
        raise DeserializationError("PublishBatchInput.topic_arn required")
    child_publish_batch_request_entries = el.find("PublishBatchRequestEntries")
    if child_publish_batch_request_entries is not None:
        import aws_sdk_sns.types.publish_batch_request_entry_list

        out["publish_batch_request_entries"] = (
            aws_sdk_sns.types.publish_batch_request_entry_list.deserialize_query(
                child_publish_batch_request_entries
            )
        )
    else:
        raise DeserializationError(
            "PublishBatchInput.publish_batch_request_entries required"
        )
    return out
