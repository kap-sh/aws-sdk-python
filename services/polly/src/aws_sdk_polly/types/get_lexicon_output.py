"""Generated from Smithy shape ``com.amazonaws.polly#GetLexiconOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_polly.types.lexicon
    import aws_sdk_polly.types.lexicon_attributes


class GetLexiconOutput(TypedDict, closed=True):
    lexicon: NotRequired["aws_sdk_polly.types.lexicon.Lexicon"]
    """<p>Lexicon object that provides name and the string content of the lexicon. </p>"""
    lexicon_attributes: NotRequired[
        "aws_sdk_polly.types.lexicon_attributes.LexiconAttributes"
    ]
    """<p>Metadata of the lexicon, including phonetic alphabetic used, language code, lexicon ARN, number of lexemes defined in the lexicon, and size of lexicon in bytes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLexiconOutput) -> dict:
    out: dict = {}
    if "lexicon" in value:
        import aws_sdk_polly.types.lexicon

        out["Lexicon"] = aws_sdk_polly.types.lexicon.serialize_json(value["lexicon"])
    if "lexicon_attributes" in value:
        import aws_sdk_polly.types.lexicon_attributes

        out["LexiconAttributes"] = (
            aws_sdk_polly.types.lexicon_attributes.serialize_json(
                value["lexicon_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetLexiconOutput:
    out: GetLexiconOutput = {}  # type: ignore[typeddict-item]
    if "Lexicon" in data:
        import aws_sdk_polly.types.lexicon

        out["lexicon"] = aws_sdk_polly.types.lexicon.deserialize_json(data["Lexicon"])
    if "LexiconAttributes" in data:
        import aws_sdk_polly.types.lexicon_attributes

        out["lexicon_attributes"] = (
            aws_sdk_polly.types.lexicon_attributes.deserialize_json(
                data["LexiconAttributes"]
            )
        )
    return out
