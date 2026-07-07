"""Generated from Smithy shape ``com.amazonaws.ses#UpdateReceiptRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.receipt_rule
    import aws_sdk_ses.types.receipt_rule_set_name


class UpdateReceiptRuleRequest(TypedDict, closed=True):
    rule_set_name: "aws_sdk_ses.types.receipt_rule_set_name.ReceiptRuleSetName"
    """<p>The name of the receipt rule set that the receipt rule belongs to.</p>"""
    rule: "aws_sdk_ses.types.receipt_rule.ReceiptRule"
    """<p>A data structure that contains the updated receipt rule information.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateReceiptRuleRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.RuleSetName", str(value["rule_set_name"])))
    import aws_sdk_ses.types.receipt_rule

    aws_sdk_ses.types.receipt_rule.serialize_query(
        value["rule"], pairs, f"{prefix}.Rule"
    )


def deserialize_query(el: Element) -> UpdateReceiptRuleRequest:
    out: UpdateReceiptRuleRequest = {}  # type: ignore[typeddict-item]
    child_rule_set_name = el.find("RuleSetName")
    if child_rule_set_name is not None:
        out["rule_set_name"] = str(child_rule_set_name.text or "")
    else:
        raise DeserializationError("UpdateReceiptRuleRequest.rule_set_name required")
    child_rule = el.find("Rule")
    if child_rule is not None:
        import aws_sdk_ses.types.receipt_rule

        out["rule"] = aws_sdk_ses.types.receipt_rule.deserialize_query(child_rule)
    else:
        raise DeserializationError("UpdateReceiptRuleRequest.rule required")
    return out
