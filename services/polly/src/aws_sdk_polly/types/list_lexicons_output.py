"""Generated from Smithy shape ``com.amazonaws.polly#ListLexiconsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_polly.types.lexicon_description_list
    import aws_sdk_polly.types.next_token


class ListLexiconsOutput(TypedDict, closed=True):
    lexicons: NotRequired[
        "aws_sdk_polly.types.lexicon_description_list.LexiconDescriptionList"
    ]
    """<p>A list of lexicon names and attributes.</p>"""
    next_token: NotRequired["aws_sdk_polly.types.next_token.NextToken"]
    """<p>The pagination token to use in the next request to continue the listing of lexicons. <code>NextToken</code> is returned only if the response is truncated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLexiconsOutput) -> dict:
    out: dict = {}
    if "lexicons" in value:
        import aws_sdk_polly.types.lexicon_description_list

        out["Lexicons"] = aws_sdk_polly.types.lexicon_description_list.serialize_json(
            value["lexicons"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLexiconsOutput:
    out: ListLexiconsOutput = {}  # type: ignore[typeddict-item]
    if "Lexicons" in data:
        import aws_sdk_polly.types.lexicon_description_list

        out["lexicons"] = aws_sdk_polly.types.lexicon_description_list.deserialize_json(
            data["Lexicons"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
