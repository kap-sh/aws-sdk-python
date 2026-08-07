"""Generated from Smithy shape ``com.amazonaws.ses#ListReceiptRuleSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.next_token
    import capo_ses.types.receipt_rule_sets_lists


class ListReceiptRuleSetsResponse(TypedDict, closed=True):
    rule_sets: NotRequired[
        "capo_ses.types.receipt_rule_sets_lists.ReceiptRuleSetsLists"
    ]
    """<p>The metadata for the currently active receipt rule set. The metadata consists of the rule set name and the timestamp of when the rule set was created.</p>"""
    next_token: NotRequired["capo_ses.types.next_token.NextToken"]
    """<p>A token indicating that there are additional receipt rule sets available to be listed. Pass this token to successive calls of <code>ListReceiptRuleSets</code> to retrieve up to 100 receipt rule sets at a time.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListReceiptRuleSetsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "rule_sets" in value:
        import capo_ses.types.receipt_rule_sets_lists

        capo_ses.types.receipt_rule_sets_lists.serialize_query(
            value["rule_sets"], pairs, f"{key_prefix}RuleSets"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListReceiptRuleSetsResponse:
    out: ListReceiptRuleSetsResponse = {}  # type: ignore[typeddict-item]
    child_rule_sets = el.find("RuleSets")
    if child_rule_sets is not None:
        import capo_ses.types.receipt_rule_sets_lists

        out["rule_sets"] = capo_ses.types.receipt_rule_sets_lists.deserialize_query(
            child_rule_sets
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
