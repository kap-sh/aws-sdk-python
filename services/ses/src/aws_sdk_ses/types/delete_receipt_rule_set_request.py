"""Generated from Smithy shape ``com.amazonaws.ses#DeleteReceiptRuleSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.receipt_rule_set_name


class DeleteReceiptRuleSetRequest(TypedDict):
    rule_set_name: "aws_sdk_ses.types.receipt_rule_set_name.ReceiptRuleSetName"
    """<p>The name of the receipt rule set to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteReceiptRuleSetRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.RuleSetName", str(value["rule_set_name"])))


def deserialize_query(el: Element) -> DeleteReceiptRuleSetRequest:
    out: DeleteReceiptRuleSetRequest = {}  # type: ignore[typeddict-item]
    child_rule_set_name = el.find("RuleSetName")
    if child_rule_set_name is not None:
        out["rule_set_name"] = str(child_rule_set_name.text or "")
    else:
        raise DeserializationError("DeleteReceiptRuleSetRequest.rule_set_name required")
    return out
