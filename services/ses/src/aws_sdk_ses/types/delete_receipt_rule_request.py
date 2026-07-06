"""Generated from Smithy shape ``com.amazonaws.ses#DeleteReceiptRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.receipt_rule_name
    import aws_sdk_ses.types.receipt_rule_set_name


class DeleteReceiptRuleRequest(TypedDict, closed=True):
    rule_set_name: "aws_sdk_ses.types.receipt_rule_set_name.ReceiptRuleSetName"
    """<p>The name of the receipt rule set that contains the receipt rule to delete.</p>"""
    rule_name: "aws_sdk_ses.types.receipt_rule_name.ReceiptRuleName"
    """<p>The name of the receipt rule to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteReceiptRuleRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.RuleSetName", str(value["rule_set_name"])))
    pairs.append((f"{prefix}.RuleName", str(value["rule_name"])))


def deserialize_query(el: Element) -> DeleteReceiptRuleRequest:
    out: DeleteReceiptRuleRequest = {}  # type: ignore[typeddict-item]
    child_rule_set_name = el.find("RuleSetName")
    if child_rule_set_name is not None:
        out["rule_set_name"] = str(child_rule_set_name.text or "")
    else:
        raise DeserializationError("DeleteReceiptRuleRequest.rule_set_name required")
    child_rule_name = el.find("RuleName")
    if child_rule_name is not None:
        out["rule_name"] = str(child_rule_name.text or "")
    else:
        raise DeserializationError("DeleteReceiptRuleRequest.rule_name required")
    return out
