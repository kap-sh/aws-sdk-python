"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchDetectKeyPhrasesItemResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.integer
    import aws_sdk_comprehend.types.list_of_key_phrases


class BatchDetectKeyPhrasesItemResult(TypedDict, closed=True):
    index: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>The zero-based index of the document in the input list.</p>"""
    key_phrases: NotRequired[
        "aws_sdk_comprehend.types.list_of_key_phrases.ListOfKeyPhrases"
    ]
    """<p>One or more <a>KeyPhrase</a> objects, one for each key phrase detected in the document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDetectKeyPhrasesItemResult) -> dict:
    out: dict = {}
    if "index" in value:
        out["Index"] = value["index"]
    if "key_phrases" in value:
        import aws_sdk_comprehend.types.list_of_key_phrases

        out["KeyPhrases"] = (
            aws_sdk_comprehend.types.list_of_key_phrases.serialize_aws_json_1_1(
                value["key_phrases"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDetectKeyPhrasesItemResult:
    out: BatchDetectKeyPhrasesItemResult = {}  # type: ignore[typeddict-item]
    if "Index" in data:
        out["index"] = data["Index"]
    if "KeyPhrases" in data:
        import aws_sdk_comprehend.types.list_of_key_phrases

        out["key_phrases"] = (
            aws_sdk_comprehend.types.list_of_key_phrases.deserialize_aws_json_1_1(
                data["KeyPhrases"]
            )
        )
    return out
