"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#QueueList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.queue

QueueList: TypeAlias = list["capo_elastic_beanstalk.types.queue.Queue"]


# --- awsQuery ser/de ---
def serialize_query(
    value: QueueList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.queue

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.queue.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> QueueList:
    import capo_elastic_beanstalk.types.queue

    out: QueueList = []
    for child in el.findall("member"):
        out.append(capo_elastic_beanstalk.types.queue.deserialize_query(child))
    return out


def serialize_query_flat(
    value: QueueList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.queue

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.queue.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> QueueList:
    import capo_elastic_beanstalk.types.queue

    out: QueueList = []
    for child in parent.findall(tag):
        out.append(capo_elastic_beanstalk.types.queue.deserialize_query(child))
    return out
