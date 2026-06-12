"""Generated from Smithy shape ``com.amazonaws.ses#ReceiptRuleSetsLists``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.receipt_rule_set_metadata

ReceiptRuleSetsLists: TypeAlias = list[
    "aws_sdk_ses.types.receipt_rule_set_metadata.ReceiptRuleSetMetadata"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReceiptRuleSetsLists, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.receipt_rule_set_metadata

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.receipt_rule_set_metadata.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ReceiptRuleSetsLists:
    import aws_sdk_ses.types.receipt_rule_set_metadata

    out: ReceiptRuleSetsLists = []
    for child in el.findall("member"):
        out.append(aws_sdk_ses.types.receipt_rule_set_metadata.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ReceiptRuleSetsLists, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.receipt_rule_set_metadata

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.receipt_rule_set_metadata.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ReceiptRuleSetsLists:
    import aws_sdk_ses.types.receipt_rule_set_metadata

    out: ReceiptRuleSetsLists = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ses.types.receipt_rule_set_metadata.deserialize_query(child))
    return out
