"""Generated from Smithy shape ``com.amazonaws.ses#ListReceiptRuleSetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.next_token


class ListReceiptRuleSetsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_ses.types.next_token.NextToken"]
    """<p>A token returned from a previous call to <code>ListReceiptRuleSets</code> to indicate the position in the receipt rule set list.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListReceiptRuleSetsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListReceiptRuleSetsRequest:
    out: ListReceiptRuleSetsRequest = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
