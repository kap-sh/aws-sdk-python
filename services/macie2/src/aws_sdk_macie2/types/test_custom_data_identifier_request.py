"""Generated from Smithy shape ``com.amazonaws.macie2#TestCustomDataIdentifierRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__integer
    import aws_sdk_macie2.types.__list_of__string
    import aws_sdk_macie2.types.__string


class TestCustomDataIdentifierRequest(TypedDict, closed=True):
    ignore_words: NotRequired["aws_sdk_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array that lists specific character sequences (<i>ignore words</i>) to exclude from the results. If the text matched by the regular expression contains any string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4-90 UTF-8 characters. Ignore words are case sensitive.</p>"""
    keywords: NotRequired["aws_sdk_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array that lists specific character sequences (<i>keywords</i>), one of which must precede and be within proximity (maximumMatchDistance) of the regular expression to match. The array can contain as many as 50 keywords. Each keyword can contain 3-90 UTF-8 characters. Keywords aren't case sensitive.</p>"""
    maximum_match_distance: NotRequired["aws_sdk_macie2.types.__integer.__integer"]
    """<p>The maximum number of characters that can exist between the end of at least one complete character sequence specified by the keywords array and the end of the text that matches the regex pattern. If a complete keyword precedes all the text that matches the pattern and the keyword is within the specified distance, Amazon Macie includes the result. The distance can be 1-300 characters. The default value is 50.</p>"""
    regex: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The regular expression (<i>regex</i>) that defines the pattern to match. The expression can contain as many as 512 characters.</p>"""
    sample_text: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The sample text to inspect by using the custom data identifier. The text can contain as many as 1,000 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestCustomDataIdentifierRequest) -> dict:
    out: dict = {}
    if "ignore_words" in value:
        import aws_sdk_macie2.types.__list_of__string

        out["ignoreWords"] = aws_sdk_macie2.types.__list_of__string.serialize_json(
            value["ignore_words"]
        )
    if "keywords" in value:
        import aws_sdk_macie2.types.__list_of__string

        out["keywords"] = aws_sdk_macie2.types.__list_of__string.serialize_json(
            value["keywords"]
        )
    if "maximum_match_distance" in value:
        out["maximumMatchDistance"] = value["maximum_match_distance"]
    if "regex" in value:
        out["regex"] = value["regex"]
    if "sample_text" in value:
        out["sampleText"] = value["sample_text"]
    return out


def deserialize_json(data: dict) -> TestCustomDataIdentifierRequest:
    out: TestCustomDataIdentifierRequest = {}  # type: ignore[typeddict-item]
    if "ignoreWords" in data:
        import aws_sdk_macie2.types.__list_of__string

        out["ignore_words"] = aws_sdk_macie2.types.__list_of__string.deserialize_json(
            data["ignoreWords"]
        )
    if "keywords" in data:
        import aws_sdk_macie2.types.__list_of__string

        out["keywords"] = aws_sdk_macie2.types.__list_of__string.deserialize_json(
            data["keywords"]
        )
    if "maximumMatchDistance" in data:
        out["maximum_match_distance"] = data["maximumMatchDistance"]
    if "regex" in data:
        out["regex"] = data["regex"]
    if "sampleText" in data:
        out["sample_text"] = data["sampleText"]
    return out
