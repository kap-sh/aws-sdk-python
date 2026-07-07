"""Generated from Smithy shape ``com.amazonaws.outposts#GetQuoteOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.quote


class GetQuoteOutput(TypedDict, closed=True):
    quote: NotRequired["aws_sdk_outposts.types.quote.Quote"]
    """<p>Information about the quote.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQuoteOutput) -> dict:
    out: dict = {}
    if "quote" in value:
        import aws_sdk_outposts.types.quote

        out["Quote"] = aws_sdk_outposts.types.quote.serialize_json(value["quote"])
    return out


def deserialize_json(data: dict) -> GetQuoteOutput:
    out: GetQuoteOutput = {}  # type: ignore[typeddict-item]
    if "Quote" in data:
        import aws_sdk_outposts.types.quote

        out["quote"] = aws_sdk_outposts.types.quote.deserialize_json(data["Quote"])
    return out
