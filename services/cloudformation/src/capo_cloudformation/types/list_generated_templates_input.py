"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListGeneratedTemplatesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.max_results
    import capo_cloudformation.types.next_token


class ListGeneratedTemplatesInput(TypedDict, closed=True):
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired["capo_cloudformation.types.max_results.MaxResults"]
    """<p>If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can use for the <code>NextToken</code> parameter to get the next set of results. By default the <code>ListGeneratedTemplates</code> API action will return at most 50 results in each response. The maximum value is 100.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListGeneratedTemplatesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))


def deserialize_query(el: Element) -> ListGeneratedTemplatesInput:
    out: ListGeneratedTemplatesInput = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
