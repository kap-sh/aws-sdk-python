"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeTopicPartitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of_topic_partition_info
    import aws_sdk_kafka.types.__string


class DescribeTopicPartitionsResponse(TypedDict, closed=True):
    partitions: NotRequired[
        "aws_sdk_kafka.types.__list_of_topic_partition_info.__listOfTopicPartitionInfo"
    ]
    """<p>The list of partition information for the topic.</p>"""
    next_token: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The paginated results marker. When the result of a DescribeTopicPartitions operation is truncated, the call returns NextToken in the response. To get another batch of configurations, provide this token in your next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTopicPartitionsResponse) -> dict:
    out: dict = {}
    if "partitions" in value:
        import aws_sdk_kafka.types.__list_of_topic_partition_info

        out["partitions"] = (
            aws_sdk_kafka.types.__list_of_topic_partition_info.serialize_json(
                value["partitions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeTopicPartitionsResponse:
    out: DescribeTopicPartitionsResponse = {}  # type: ignore[typeddict-item]
    if "partitions" in data:
        import aws_sdk_kafka.types.__list_of_topic_partition_info

        out["partitions"] = (
            aws_sdk_kafka.types.__list_of_topic_partition_info.deserialize_json(
                data["partitions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
