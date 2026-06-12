"""Generated from Smithy shape ``com.amazonaws.ses#ReceiptRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.receipt_rule

ReceiptRulesList: TypeAlias = list["aws_sdk_ses.types.receipt_rule.ReceiptRule"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReceiptRulesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.receipt_rule

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.receipt_rule.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ReceiptRulesList:
    import aws_sdk_ses.types.receipt_rule

    out: ReceiptRulesList = []
    for child in el.findall("member"):
        out.append(aws_sdk_ses.types.receipt_rule.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ReceiptRulesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.receipt_rule

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.receipt_rule.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ReceiptRulesList:
    import aws_sdk_ses.types.receipt_rule

    out: ReceiptRulesList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ses.types.receipt_rule.deserialize_query(child))
    return out
