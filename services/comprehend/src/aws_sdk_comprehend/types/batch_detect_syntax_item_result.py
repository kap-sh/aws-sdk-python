"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchDetectSyntaxItemResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.integer
    import aws_sdk_comprehend.types.list_of_syntax_tokens


class BatchDetectSyntaxItemResult(TypedDict):
    index: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>The zero-based index of the document in the input list.</p>"""
    syntax_tokens: NotRequired[
        "aws_sdk_comprehend.types.list_of_syntax_tokens.ListOfSyntaxTokens"
    ]
    """<p>The syntax tokens for the words in the document, one token for each word.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDetectSyntaxItemResult) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "syntax_tokens" in value:
        import aws_sdk_comprehend.types.list_of_syntax_tokens

        out["SyntaxTokens"] = (
            aws_sdk_comprehend.types.list_of_syntax_tokens.serialize_aws_json_1_1(
                value["syntax_tokens"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDetectSyntaxItemResult:
    out: BatchDetectSyntaxItemResult = {}  # type: ignore[typeddict-item]
    if "Index" in data:
        out["index"] = data["Index"]
    if "SyntaxTokens" in data:
        import aws_sdk_comprehend.types.list_of_syntax_tokens

        out["syntax_tokens"] = (
            aws_sdk_comprehend.types.list_of_syntax_tokens.deserialize_aws_json_1_1(
                data["SyntaxTokens"]
            )
        )
    return out
