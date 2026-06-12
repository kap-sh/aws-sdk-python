"""Generated from Smithy shape ``com.amazonaws.sns#ListTopicsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.next_token
    import aws_sdk_sns.types.topics_list


class ListTopicsResponse(TypedDict):
    topics: NotRequired["aws_sdk_sns.types.topics_list.TopicsList"]
    """<p>A list of topic ARNs.</p>"""
    next_token: NotRequired["aws_sdk_sns.types.next_token.nextToken"]
    """<p>Token to pass along to the next <code>ListTopics</code> request. This element is returned if there are additional topics to retrieve.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListTopicsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "topics" in value:
        import aws_sdk_sns.types.topics_list

        aws_sdk_sns.types.topics_list.serialize_query(
            value["topics"], pairs, f"{prefix}.Topics"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListTopicsResponse:
    out: ListTopicsResponse = {}  # type: ignore[typeddict-item]
    child_topics = el.find("Topics")
    if child_topics is not None:
        import aws_sdk_sns.types.topics_list

        out["topics"] = aws_sdk_sns.types.topics_list.deserialize_query(child_topics)
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
