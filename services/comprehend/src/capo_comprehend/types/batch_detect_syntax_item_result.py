"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchDetectSyntaxItemResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.integer
    import capo_comprehend.types.list_of_syntax_tokens


class BatchDetectSyntaxItemResult(TypedDict, closed=True):
    index: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The zero-based index of the document in the input list.</p>"""
    syntax_tokens: NotRequired[
        "capo_comprehend.types.list_of_syntax_tokens.ListOfSyntaxTokens"
    ]
    """<p>The syntax tokens for the words in the document, one token for each word.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDetectSyntaxItemResult) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "syntax_tokens" in value:
        import capo_comprehend.types.list_of_syntax_tokens

        out["SyntaxTokens"] = (
            capo_comprehend.types.list_of_syntax_tokens.serialize_aws_json_1_1(
                value["syntax_tokens"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDetectSyntaxItemResult:
    out: BatchDetectSyntaxItemResult = {}  # type: ignore[typeddict-item]
    if "Index" in data:
        out["index"] = data["Index"]
    if "SyntaxTokens" in data:
        import capo_comprehend.types.list_of_syntax_tokens

        out["syntax_tokens"] = (
            capo_comprehend.types.list_of_syntax_tokens.deserialize_aws_json_1_1(
                data["SyntaxTokens"]
            )
        )
    return out
