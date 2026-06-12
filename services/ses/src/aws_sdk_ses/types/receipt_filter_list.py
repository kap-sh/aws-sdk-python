"""Generated from Smithy shape ``com.amazonaws.ses#ReceiptFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.receipt_filter

ReceiptFilterList: TypeAlias = list["aws_sdk_ses.types.receipt_filter.ReceiptFilter"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReceiptFilterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.receipt_filter

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.receipt_filter.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ReceiptFilterList:
    import aws_sdk_ses.types.receipt_filter

    out: ReceiptFilterList = []
    for child in el.findall("member"):
        out.append(aws_sdk_ses.types.receipt_filter.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ReceiptFilterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.receipt_filter

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.receipt_filter.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ReceiptFilterList:
    import aws_sdk_ses.types.receipt_filter

    out: ReceiptFilterList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ses.types.receipt_filter.deserialize_query(child))
    return out
