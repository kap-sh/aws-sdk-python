"""Generated from Smithy shape ``com.amazonaws.sns#ListTopicsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.next_token


class ListTopicsInput(TypedDict, closed=True):
    next_token: NotRequired["capo_sns.types.next_token.nextToken"]
    """<p>Token returned by the previous <code>ListTopics</code> request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListTopicsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListTopicsInput:
    out: ListTopicsInput = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
