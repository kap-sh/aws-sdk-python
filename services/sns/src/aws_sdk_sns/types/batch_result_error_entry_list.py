"""Generated from Smithy shape ``com.amazonaws.sns#BatchResultErrorEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.batch_result_error_entry

BatchResultErrorEntryList: TypeAlias = list[
    "aws_sdk_sns.types.batch_result_error_entry.BatchResultErrorEntry"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchResultErrorEntryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_sns.types.batch_result_error_entry

    for n, item in enumerate(value, 1):
        aws_sdk_sns.types.batch_result_error_entry.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> BatchResultErrorEntryList:
    import aws_sdk_sns.types.batch_result_error_entry

    out: BatchResultErrorEntryList = []
    for child in el.findall("member"):
        out.append(aws_sdk_sns.types.batch_result_error_entry.deserialize_query(child))
    return out


def serialize_query_flat(
    value: BatchResultErrorEntryList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_sns.types.batch_result_error_entry

    for n, item in enumerate(value, 1):
        aws_sdk_sns.types.batch_result_error_entry.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> BatchResultErrorEntryList:
    import aws_sdk_sns.types.batch_result_error_entry

    out: BatchResultErrorEntryList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_sns.types.batch_result_error_entry.deserialize_query(child))
    return out
