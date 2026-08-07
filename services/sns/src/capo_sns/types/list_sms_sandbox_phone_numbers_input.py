"""Generated from Smithy shape ``com.amazonaws.sns#ListSMSSandboxPhoneNumbersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.max_items
    import capo_sns.types.next_token


class ListSMSSandboxPhoneNumbersInput(TypedDict, closed=True):
    next_token: NotRequired["capo_sns.types.next_token.nextToken"]
    """<p>Token that the previous <code>ListSMSSandboxPhoneNumbersInput</code> request returns.</p>"""
    max_results: NotRequired["capo_sns.types.max_items.MaxItems"]
    """<p>The maximum number of phone numbers to return.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListSMSSandboxPhoneNumbersInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))


def deserialize_query(el: Element) -> ListSMSSandboxPhoneNumbersInput:
    out: ListSMSSandboxPhoneNumbersInput = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
