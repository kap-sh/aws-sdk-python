"""Generated from Smithy shape ``com.amazonaws.outposts#GetQuoteInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.quote_identifier


class GetQuoteInput(TypedDict):
    quote_identifier: "aws_sdk_outposts.types.quote_identifier.QuoteIdentifier"
    """<p>The ID or ARN of the quote.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQuoteInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQuoteInput:
    out: GetQuoteInput = {}  # type: ignore[typeddict-item]
    return out
