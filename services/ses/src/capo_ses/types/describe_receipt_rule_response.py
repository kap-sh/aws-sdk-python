"""Generated from Smithy shape ``com.amazonaws.ses#DescribeReceiptRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.receipt_rule


class DescribeReceiptRuleResponse(TypedDict, closed=True):
    rule: NotRequired["capo_ses.types.receipt_rule.ReceiptRule"]
    """<p>A data structure that contains the specified receipt rule's name, actions, recipients, domains, enabled status, scan status, and Transport Layer Security (TLS) policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeReceiptRuleResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "rule" in value:
        import capo_ses.types.receipt_rule

        capo_ses.types.receipt_rule.serialize_query(
            value["rule"], pairs, f"{key_prefix}Rule"
        )


def deserialize_query(el: Element) -> DescribeReceiptRuleResponse:
    out: DescribeReceiptRuleResponse = {}  # type: ignore[typeddict-item]
    child_rule = el.find("Rule")
    if child_rule is not None:
        import capo_ses.types.receipt_rule

        out["rule"] = capo_ses.types.receipt_rule.deserialize_query(child_rule)
    return out
