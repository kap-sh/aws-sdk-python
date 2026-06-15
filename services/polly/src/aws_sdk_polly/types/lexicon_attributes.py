"""Generated from Smithy shape ``com.amazonaws.polly#LexiconAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_polly.types.alphabet
    import aws_sdk_polly.types.language_code
    import aws_sdk_polly.types.last_modified
    import aws_sdk_polly.types.lexemes_count
    import aws_sdk_polly.types.lexicon_arn
    import aws_sdk_polly.types.size


class LexiconAttributes(TypedDict):
    alphabet: NotRequired["aws_sdk_polly.types.alphabet.Alphabet"]
    """<p>Phonetic alphabet used in the lexicon. Valid values are <code>ipa</code> and <code>x-sampa</code>.</p>"""
    language_code: NotRequired["aws_sdk_polly.types.language_code.LanguageCode"]
    r"""<p>Language code that the lexicon applies to. A lexicon with a language code such as \"en\" would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so on.</p>"""
    last_modified: NotRequired["aws_sdk_polly.types.last_modified.LastModified"]
    """<p>Date lexicon was last modified (a timestamp value).</p>"""
    lexicon_arn: NotRequired["aws_sdk_polly.types.lexicon_arn.LexiconArn"]
    """<p>Amazon Resource Name (ARN) of the lexicon.</p>"""
    lexemes_count: "aws_sdk_polly.types.lexemes_count.LexemesCount"
    """<p>Number of lexemes in the lexicon.</p>"""
    size: "aws_sdk_polly.types.size.Size"
    """<p>Total size of the lexicon, in characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LexiconAttributes) -> dict:
    out: dict = {}
    if "alphabet" in value:
        out["Alphabet"] = value["alphabet"]
    if "language_code" in value:
        import aws_sdk_polly.types.language_code

        out["LanguageCode"] = aws_sdk_polly.types.language_code.serialize_json(
            value["language_code"]
        )
    if "last_modified" in value:
        import aws_sdk_polly.types.last_modified

        out["LastModified"] = aws_sdk_polly.types.last_modified.serialize_json(
            value["last_modified"]
        )
    if "lexicon_arn" in value:
        out["LexiconArn"] = value["lexicon_arn"]
    out["LexemesCount"] = value.get("lexemes_count", 0)
    out["Size"] = value.get("size", 0)
    return out


def deserialize_json(data: dict) -> LexiconAttributes:
    out: LexiconAttributes = {}  # type: ignore[typeddict-item]
    if "Alphabet" in data:
        out["alphabet"] = data["Alphabet"]
    if "LanguageCode" in data:
        import aws_sdk_polly.types.language_code

        out["language_code"] = aws_sdk_polly.types.language_code.deserialize_json(
            data["LanguageCode"]
        )
    if "LastModified" in data:
        import aws_sdk_polly.types.last_modified

        out["last_modified"] = aws_sdk_polly.types.last_modified.deserialize_json(
            data["LastModified"]
        )
    if "LexiconArn" in data:
        out["lexicon_arn"] = data["LexiconArn"]
    if "LexemesCount" in data:
        out["lexemes_count"] = data["LexemesCount"]
    else:
        out["lexemes_count"] = 0
    if "Size" in data:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    return out
