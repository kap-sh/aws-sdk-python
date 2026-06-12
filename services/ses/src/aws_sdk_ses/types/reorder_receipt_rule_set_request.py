"""Generated from Smithy shape ``com.amazonaws.ses#ReorderReceiptRuleSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.receipt_rule_names_list
    import aws_sdk_ses.types.receipt_rule_set_name


class ReorderReceiptRuleSetRequest(TypedDict):
    rule_set_name: "aws_sdk_ses.types.receipt_rule_set_name.ReceiptRuleSetName"
    """<p>The name of the receipt rule set to reorder.</p>"""
    rule_names: "aws_sdk_ses.types.receipt_rule_names_list.ReceiptRuleNamesList"
    """<p>The specified receipt rule set's receipt rules, in order.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReorderReceiptRuleSetRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.RuleSetName", str(value["rule_set_name"])))
    import aws_sdk_ses.types.receipt_rule_names_list

    aws_sdk_ses.types.receipt_rule_names_list.serialize_query(
        value["rule_names"], pairs, f"{prefix}.RuleNames"
    )


def deserialize_query(el: Element) -> ReorderReceiptRuleSetRequest:
    out: ReorderReceiptRuleSetRequest = {}  # type: ignore[typeddict-item]
    child_rule_set_name = el.find("RuleSetName")
    if child_rule_set_name is not None:
        out["rule_set_name"] = str(child_rule_set_name.text or "")
    else:
        raise DeserializationError(
            "ReorderReceiptRuleSetRequest.rule_set_name required"
        )
    child_rule_names = el.find("RuleNames")
    if child_rule_names is not None:
        import aws_sdk_ses.types.receipt_rule_names_list

        out["rule_names"] = aws_sdk_ses.types.receipt_rule_names_list.deserialize_query(
            child_rule_names
        )
    else:
        raise DeserializationError("ReorderReceiptRuleSetRequest.rule_names required")
    return out
