"""Generated from Smithy shape ``com.amazonaws.ses#ReceiptRuleSetsLists``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.receipt_rule_set_metadata

ReceiptRuleSetsLists: TypeAlias = list[
    "capo_ses.types.receipt_rule_set_metadata.ReceiptRuleSetMetadata"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReceiptRuleSetsLists, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.receipt_rule_set_metadata

    for n, item in enumerate(value, 1):
        capo_ses.types.receipt_rule_set_metadata.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ReceiptRuleSetsLists:
    import capo_ses.types.receipt_rule_set_metadata

    out: ReceiptRuleSetsLists = []
    for child in el.findall("member"):
        out.append(capo_ses.types.receipt_rule_set_metadata.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ReceiptRuleSetsLists, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.receipt_rule_set_metadata

    for n, item in enumerate(value, 1):
        capo_ses.types.receipt_rule_set_metadata.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ReceiptRuleSetsLists:
    import capo_ses.types.receipt_rule_set_metadata

    out: ReceiptRuleSetsLists = []
    for child in parent.findall(tag):
        out.append(capo_ses.types.receipt_rule_set_metadata.deserialize_query(child))
    return out
