"""Generated from Smithy shape ``com.amazonaws.outposts#GetQuoteInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.quote_identifier


class GetQuoteInput(TypedDict, closed=True):
    quote_identifier: "capo_outposts.types.quote_identifier.QuoteIdentifier"
    """<p>The ID or ARN of the quote.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQuoteInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQuoteInput:
    out: GetQuoteInput = {}  # type: ignore[typeddict-item]
    return out
