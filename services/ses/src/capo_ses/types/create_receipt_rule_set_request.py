"""Generated from Smithy shape ``com.amazonaws.ses#CreateReceiptRuleSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.receipt_rule_set_name


class CreateReceiptRuleSetRequest(TypedDict, closed=True):
    rule_set_name: "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName"
    """<p>The name of the rule set to create. The name must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).</p> </li> <li> <p>Start and end with a letter or number.</p> </li> <li> <p>Contain 64 characters or fewer.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateReceiptRuleSetRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.RuleSetName", str(value["rule_set_name"])))


def deserialize_query(el: Element) -> CreateReceiptRuleSetRequest:
    out: CreateReceiptRuleSetRequest = {}  # type: ignore[typeddict-item]
    child_rule_set_name = el.find("RuleSetName")
    if child_rule_set_name is not None:
        out["rule_set_name"] = str(child_rule_set_name.text or "")
    else:
        raise DeserializationError("CreateReceiptRuleSetRequest.rule_set_name required")
    return out
