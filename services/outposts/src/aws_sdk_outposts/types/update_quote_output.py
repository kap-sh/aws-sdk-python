"""Generated from Smithy shape ``com.amazonaws.outposts#UpdateQuoteOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.quote


class UpdateQuoteOutput(TypedDict):
    quote: NotRequired["aws_sdk_outposts.types.quote.Quote"]
    """<p>Information about the updated quote.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQuoteOutput) -> dict:
    out: dict = {}
    if "quote" in value:
        import aws_sdk_outposts.types.quote

        out["Quote"] = aws_sdk_outposts.types.quote.serialize_json(value["quote"])
    return out


def deserialize_json(data: dict) -> UpdateQuoteOutput:
    out: UpdateQuoteOutput = {}  # type: ignore[typeddict-item]
    if "Quote" in data:
        import aws_sdk_outposts.types.quote

        out["quote"] = aws_sdk_outposts.types.quote.deserialize_json(data["Quote"])
    return out
