"""Generated from Smithy shape ``com.amazonaws.comprehend#SyntaxToken``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.integer
    import aws_sdk_comprehend.types.part_of_speech_tag
    import aws_sdk_comprehend.types.string


class SyntaxToken(TypedDict):
    token_id: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>A unique identifier for a token.</p>"""
    text: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>The word that was recognized in the source text.</p>"""
    begin_offset: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>The zero-based offset from the beginning of the source text to the first character in the word.</p>"""
    end_offset: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>The zero-based offset from the beginning of the source text to the last character in the word.</p>"""
    part_of_speech: NotRequired[
        "aws_sdk_comprehend.types.part_of_speech_tag.PartOfSpeechTag"
    ]
    r"""<p>Provides the part of speech label and the confidence level that Amazon Comprehend has that the part of speech was correctly identified. For more information, see <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/how-syntax.html\">Syntax</a> in the Comprehend Developer Guide. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SyntaxToken) -> dict:
    out: dict = {}
    if "token_id" in value:
        out["TokenId"] = value["token_id"]
    if "text" in value:
        out["Text"] = value["text"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    if "part_of_speech" in value:
        import aws_sdk_comprehend.types.part_of_speech_tag

        out["PartOfSpeech"] = (
            aws_sdk_comprehend.types.part_of_speech_tag.serialize_aws_json_1_1(
                value["part_of_speech"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SyntaxToken:
    out: SyntaxToken = {}  # type: ignore[typeddict-item]
    if "TokenId" in data:
        out["token_id"] = data["TokenId"]
    if "Text" in data:
        out["text"] = data["Text"]
    if "BeginOffset" in data:
        out["begin_offset"] = data["BeginOffset"]
    if "EndOffset" in data:
        out["end_offset"] = data["EndOffset"]
    if "PartOfSpeech" in data:
        import aws_sdk_comprehend.types.part_of_speech_tag

        out["part_of_speech"] = (
            aws_sdk_comprehend.types.part_of_speech_tag.deserialize_aws_json_1_1(
                data["PartOfSpeech"]
            )
        )
    return out
