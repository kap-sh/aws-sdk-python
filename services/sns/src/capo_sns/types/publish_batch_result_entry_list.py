"""Generated from Smithy shape ``com.amazonaws.sns#PublishBatchResultEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.publish_batch_result_entry

PublishBatchResultEntryList: TypeAlias = list[
    "capo_sns.types.publish_batch_result_entry.PublishBatchResultEntry"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PublishBatchResultEntryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_sns.types.publish_batch_result_entry

    for n, item in enumerate(value, 1):
        capo_sns.types.publish_batch_result_entry.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PublishBatchResultEntryList:
    import capo_sns.types.publish_batch_result_entry

    out: PublishBatchResultEntryList = []
    for child in el.findall("member"):
        out.append(capo_sns.types.publish_batch_result_entry.deserialize_query(child))
    return out


def serialize_query_flat(
    value: PublishBatchResultEntryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_sns.types.publish_batch_result_entry

    for n, item in enumerate(value, 1):
        capo_sns.types.publish_batch_result_entry.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> PublishBatchResultEntryList:
    import capo_sns.types.publish_batch_result_entry

    out: PublishBatchResultEntryList = []
    for child in parent.findall(tag):
        out.append(capo_sns.types.publish_batch_result_entry.deserialize_query(child))
    return out
