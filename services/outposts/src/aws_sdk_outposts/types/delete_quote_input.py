"""Generated from Smithy shape ``com.amazonaws.outposts#DeleteQuoteInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.quote_identifier


class DeleteQuoteInput(TypedDict, closed=True):
    quote_identifier: "aws_sdk_outposts.types.quote_identifier.QuoteIdentifier"
    """<p>The ID or ARN of the quote.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQuoteInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteQuoteInput:
    out: DeleteQuoteInput = {}  # type: ignore[typeddict-item]
    return out
