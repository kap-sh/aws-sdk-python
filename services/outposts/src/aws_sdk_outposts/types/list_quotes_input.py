"""Generated from Smithy shape ``com.amazonaws.outposts#ListQuotesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.max_results1000
    import aws_sdk_outposts.types.token


class ListQuotesInput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]
    """<p>The pagination token.</p>"""
    max_results: NotRequired["aws_sdk_outposts.types.max_results1000.MaxResults1000"]
    """<p>The maximum page size.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQuotesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListQuotesInput:
    out: ListQuotesInput = {}  # type: ignore[typeddict-item]
    return out
