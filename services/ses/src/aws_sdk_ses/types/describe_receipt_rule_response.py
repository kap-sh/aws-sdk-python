"""Generated from Smithy shape ``com.amazonaws.ses#DescribeReceiptRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.receipt_rule


class DescribeReceiptRuleResponse(TypedDict, closed=True):
    rule: NotRequired["aws_sdk_ses.types.receipt_rule.ReceiptRule"]
    """<p>A data structure that contains the specified receipt rule's name, actions, recipients, domains, enabled status, scan status, and Transport Layer Security (TLS) policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeReceiptRuleResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "rule" in value:
        import aws_sdk_ses.types.receipt_rule

        aws_sdk_ses.types.receipt_rule.serialize_query(
            value["rule"], pairs, f"{prefix}.Rule"
        )


def deserialize_query(el: Element) -> DescribeReceiptRuleResponse:
    out: DescribeReceiptRuleResponse = {}  # type: ignore[typeddict-item]
    child_rule = el.find("Rule")
    if child_rule is not None:
        import aws_sdk_ses.types.receipt_rule

        out["rule"] = aws_sdk_ses.types.receipt_rule.deserialize_query(child_rule)
    return out
