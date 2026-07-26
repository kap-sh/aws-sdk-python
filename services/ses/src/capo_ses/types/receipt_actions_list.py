"""Generated from Smithy shape ``com.amazonaws.ses#ReceiptActionsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.receipt_action

ReceiptActionsList: TypeAlias = list["capo_ses.types.receipt_action.ReceiptAction"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReceiptActionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.receipt_action

    for n, item in enumerate(value, 1):
        capo_ses.types.receipt_action.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ReceiptActionsList:
    import capo_ses.types.receipt_action

    out: ReceiptActionsList = []
    for child in el.findall("member"):
        out.append(capo_ses.types.receipt_action.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ReceiptActionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.receipt_action

    for n, item in enumerate(value, 1):
        capo_ses.types.receipt_action.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ReceiptActionsList:
    import capo_ses.types.receipt_action

    out: ReceiptActionsList = []
    for child in parent.findall(tag):
        out.append(capo_ses.types.receipt_action.deserialize_query(child))
    return out
