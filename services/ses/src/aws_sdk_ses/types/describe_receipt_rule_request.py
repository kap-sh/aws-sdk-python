"""Generated from Smithy shape ``com.amazonaws.ses#DescribeReceiptRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.receipt_rule_name
    import aws_sdk_ses.types.receipt_rule_set_name


class DescribeReceiptRuleRequest(TypedDict):
    rule_set_name: "aws_sdk_ses.types.receipt_rule_set_name.ReceiptRuleSetName"
    """<p>The name of the receipt rule set that the receipt rule belongs to.</p>"""
    rule_name: "aws_sdk_ses.types.receipt_rule_name.ReceiptRuleName"
    """<p>The name of the receipt rule.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeReceiptRuleRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.RuleSetName", str(value["rule_set_name"])))
    pairs.append((f"{prefix}.RuleName", str(value["rule_name"])))


def deserialize_query(el: Element) -> DescribeReceiptRuleRequest:
    out: DescribeReceiptRuleRequest = {}  # type: ignore[typeddict-item]
    child_rule_set_name = el.find("RuleSetName")
    if child_rule_set_name is not None:
        out["rule_set_name"] = str(child_rule_set_name.text or "")
    else:
        raise DeserializationError("DescribeReceiptRuleRequest.rule_set_name required")
    child_rule_name = el.find("RuleName")
    if child_rule_name is not None:
        out["rule_name"] = str(child_rule_name.text or "")
    else:
        raise DeserializationError("DescribeReceiptRuleRequest.rule_name required")
    return out
