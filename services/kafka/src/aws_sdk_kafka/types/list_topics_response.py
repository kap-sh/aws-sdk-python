"""Generated from Smithy shape ``com.amazonaws.kafka#ListTopicsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of_topic_info
    import aws_sdk_kafka.types.__string


class ListTopicsResponse(TypedDict):
    topics: NotRequired["aws_sdk_kafka.types.__list_of_topic_info.__listOfTopicInfo"]
    """<p>List containing topics info.</p>"""
    next_token: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The paginated results marker. When the result of a ListTopics operation is truncated, the call returns NextToken in the response. To get another batch of configurations, provide this token in your next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTopicsResponse) -> dict:
    out: dict = {}
    if "topics" in value:
        import aws_sdk_kafka.types.__list_of_topic_info

        out["topics"] = aws_sdk_kafka.types.__list_of_topic_info.serialize_json(
            value["topics"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTopicsResponse:
    out: ListTopicsResponse = {}  # type: ignore[typeddict-item]
    if "topics" in data:
        import aws_sdk_kafka.types.__list_of_topic_info

        out["topics"] = aws_sdk_kafka.types.__list_of_topic_info.deserialize_json(
            data["topics"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
