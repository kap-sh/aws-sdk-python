"""Generated from Smithy shape ``com.amazonaws.sns#BatchResultErrorEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.batch_result_error_entry

BatchResultErrorEntryList: TypeAlias = list[
    "capo_sns.types.batch_result_error_entry.BatchResultErrorEntry"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchResultErrorEntryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_sns.types.batch_result_error_entry

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_sns.types.batch_result_error_entry.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> BatchResultErrorEntryList:
    import capo_sns.types.batch_result_error_entry

    out: BatchResultErrorEntryList = []
    for child in el.findall("member"):
        out.append(capo_sns.types.batch_result_error_entry.deserialize_query(child))
    return out


def serialize_query_flat(
    value: BatchResultErrorEntryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_sns.types.batch_result_error_entry

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_sns.types.batch_result_error_entry.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> BatchResultErrorEntryList:
    import capo_sns.types.batch_result_error_entry

    out: BatchResultErrorEntryList = []
    for child in parent.findall(tag):
        out.append(capo_sns.types.batch_result_error_entry.deserialize_query(child))
    return out
