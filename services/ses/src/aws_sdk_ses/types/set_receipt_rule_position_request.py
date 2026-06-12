"""Generated from Smithy shape ``com.amazonaws.ses#SetReceiptRulePositionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.receipt_rule_name
    import aws_sdk_ses.types.receipt_rule_set_name


class SetReceiptRulePositionRequest(TypedDict):
    rule_set_name: "aws_sdk_ses.types.receipt_rule_set_name.ReceiptRuleSetName"
    """<p>The name of the receipt rule set that contains the receipt rule to reposition.</p>"""
    rule_name: "aws_sdk_ses.types.receipt_rule_name.ReceiptRuleName"
    """<p>The name of the receipt rule to reposition.</p>"""
    after: NotRequired["aws_sdk_ses.types.receipt_rule_name.ReceiptRuleName"]
    """<p>The name of the receipt rule after which to place the specified receipt rule.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetReceiptRulePositionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.RuleSetName", str(value["rule_set_name"])))
    pairs.append((f"{prefix}.RuleName", str(value["rule_name"])))
    if "after" in value:
        pairs.append((f"{prefix}.After", str(value["after"])))


def deserialize_query(el: Element) -> SetReceiptRulePositionRequest:
    out: SetReceiptRulePositionRequest = {}  # type: ignore[typeddict-item]
    child_rule_set_name = el.find("RuleSetName")
    if child_rule_set_name is not None:
        out["rule_set_name"] = str(child_rule_set_name.text or "")
    else:
        raise DeserializationError(
            "SetReceiptRulePositionRequest.rule_set_name required"
        )
    child_rule_name = el.find("RuleName")
    if child_rule_name is not None:
        out["rule_name"] = str(child_rule_name.text or "")
    else:
        raise DeserializationError("SetReceiptRulePositionRequest.rule_name required")
    child_after = el.find("After")
    if child_after is not None:
        out["after"] = str(child_after.text or "")
    return out
