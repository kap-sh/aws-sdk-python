"""Generated from Smithy shape ``com.amazonaws.outposts#ListQuotesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.quote_summary_list_definition
    import aws_sdk_outposts.types.token


class ListQuotesOutput(TypedDict):
    quotes: NotRequired[
        "aws_sdk_outposts.types.quote_summary_list_definition.QuoteSummaryListDefinition"
    ]
    """<p>Information about the quotes.</p>"""
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQuotesOutput) -> dict:
    out: dict = {}
    if "quotes" in value:
        import aws_sdk_outposts.types.quote_summary_list_definition

        out["Quotes"] = (
            aws_sdk_outposts.types.quote_summary_list_definition.serialize_json(
                value["quotes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListQuotesOutput:
    out: ListQuotesOutput = {}  # type: ignore[typeddict-item]
    if "Quotes" in data:
        import aws_sdk_outposts.types.quote_summary_list_definition

        out["quotes"] = (
            aws_sdk_outposts.types.quote_summary_list_definition.deserialize_json(
                data["Quotes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
