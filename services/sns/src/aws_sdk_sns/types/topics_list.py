"""Generated from Smithy shape ``com.amazonaws.sns#TopicsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.topic

TopicsList: TypeAlias = list["aws_sdk_sns.types.topic.Topic"]


# --- awsQuery ser/de ---
def serialize_query(
    value: TopicsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_sns.types.topic

    for n, item in enumerate(value, 1):
        aws_sdk_sns.types.topic.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> TopicsList:
    import aws_sdk_sns.types.topic

    out: TopicsList = []
    for child in el.findall("member"):
        out.append(aws_sdk_sns.types.topic.deserialize_query(child))
    return out


def serialize_query_flat(
    value: TopicsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_sns.types.topic

    for n, item in enumerate(value, 1):
        aws_sdk_sns.types.topic.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> TopicsList:
    import aws_sdk_sns.types.topic

    out: TopicsList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_sns.types.topic.deserialize_query(child))
    return out
