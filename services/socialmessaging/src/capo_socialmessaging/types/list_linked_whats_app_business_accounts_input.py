"""Generated from Smithy shape ``com.amazonaws.socialmessaging#ListLinkedWhatsAppBusinessAccountsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.max_results
    import capo_socialmessaging.types.next_token


class ListLinkedWhatsAppBusinessAccountsInput(TypedDict, closed=True):
    next_token: NotRequired["capo_socialmessaging.types.next_token.NextToken"]
    """<p>The next token for pagination.</p>"""
    max_results: NotRequired["capo_socialmessaging.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLinkedWhatsAppBusinessAccountsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListLinkedWhatsAppBusinessAccountsInput:
    out: ListLinkedWhatsAppBusinessAccountsInput = {}  # type: ignore[typeddict-item]
    return out
