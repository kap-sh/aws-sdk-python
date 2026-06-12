"""Generated from Smithy shape ``com.amazonaws.comprehend#DominantLanguage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.float
    import aws_sdk_comprehend.types.string


class DominantLanguage(TypedDict):
    language_code: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>The RFC 5646 language code for the dominant language. For more information about RFC 5646, see <a href=\"https://tools.ietf.org/html/rfc5646\">Tags for Identifying Languages</a> on the <i>IETF Tools</i> web site.</p>"""
    score: NotRequired["aws_sdk_comprehend.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of the detection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DominantLanguage) -> dict:
    out: dict = {}
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
    if "score" in value:
        out["Score"] = value["score"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DominantLanguage:
    out: DominantLanguage = {}  # type: ignore[typeddict-item]
    if "LanguageCode" in data:
        out["language_code"] = data["LanguageCode"]
    if "Score" in data:
        out["score"] = data["Score"]
    return out
