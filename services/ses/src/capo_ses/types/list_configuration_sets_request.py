"""Generated from Smithy shape ``com.amazonaws.ses#ListConfigurationSetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.max_items
    import capo_ses.types.next_token


class ListConfigurationSetsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_ses.types.next_token.NextToken"]
    """<p>A token returned from a previous call to <code>ListConfigurationSets</code> to indicate the position of the configuration set in the configuration set list.</p>"""
    max_items: NotRequired["capo_ses.types.max_items.MaxItems"]
    """<p>The number of configuration sets to return.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListConfigurationSetsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_items" in value:
        pairs.append((f"{key_prefix}MaxItems", str(value["max_items"])))


def deserialize_query(el: Element) -> ListConfigurationSetsRequest:
    out: ListConfigurationSetsRequest = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    return out
