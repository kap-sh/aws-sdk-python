"""Generated from Smithy shape ``com.amazonaws.sns#PublishBatchRequestEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.publish_batch_request_entry

PublishBatchRequestEntryList: TypeAlias = list[
    "capo_sns.types.publish_batch_request_entry.PublishBatchRequestEntry"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PublishBatchRequestEntryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_sns.types.publish_batch_request_entry

    for n, item in enumerate(value, 1):
        capo_sns.types.publish_batch_request_entry.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PublishBatchRequestEntryList:
    import capo_sns.types.publish_batch_request_entry

    out: PublishBatchRequestEntryList = []
    for child in el.findall("member"):
        out.append(capo_sns.types.publish_batch_request_entry.deserialize_query(child))
    return out


def serialize_query_flat(
    value: PublishBatchRequestEntryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_sns.types.publish_batch_request_entry

    for n, item in enumerate(value, 1):
        capo_sns.types.publish_batch_request_entry.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> PublishBatchRequestEntryList:
    import capo_sns.types.publish_batch_request_entry

    out: PublishBatchRequestEntryList = []
    for child in parent.findall(tag):
        out.append(capo_sns.types.publish_batch_request_entry.deserialize_query(child))
    return out
