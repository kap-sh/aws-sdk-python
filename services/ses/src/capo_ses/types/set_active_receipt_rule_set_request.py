"""Generated from Smithy shape ``com.amazonaws.ses#SetActiveReceiptRuleSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.receipt_rule_set_name


class SetActiveReceiptRuleSetRequest(TypedDict, closed=True):
    rule_set_name: NotRequired[
        "capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName"
    ]
    """<p>The name of the receipt rule set to make active. Setting this value to null disables all email receiving.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetActiveReceiptRuleSetRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "rule_set_name" in value:
        pairs.append((f"{prefix}.RuleSetName", str(value["rule_set_name"])))


def deserialize_query(el: Element) -> SetActiveReceiptRuleSetRequest:
    out: SetActiveReceiptRuleSetRequest = {}  # type: ignore[typeddict-item]
    child_rule_set_name = el.find("RuleSetName")
    if child_rule_set_name is not None:
        out["rule_set_name"] = str(child_rule_set_name.text or "")
    return out
