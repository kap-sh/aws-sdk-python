"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectDominantLanguageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.list_of_dominant_languages


class DetectDominantLanguageResponse(TypedDict, closed=True):
    languages: NotRequired[
        "aws_sdk_comprehend.types.list_of_dominant_languages.ListOfDominantLanguages"
    ]
    r"""<p>Array of languages that Amazon Comprehend detected in the input text. The array is sorted in descending order of the score (the dominant language is always the first element in the array).</p> <p>For each language, the response returns the RFC 5646 language code and the level of confidence that Amazon Comprehend has in the accuracy of its inference. For more information about RFC 5646, see <a href=\"https://tools.ietf.org/html/rfc5646\">Tags for Identifying Languages</a> on the <i>IETF Tools</i> web site.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectDominantLanguageResponse) -> dict:
    out: dict = {}
    if "languages" in value:
        import aws_sdk_comprehend.types.list_of_dominant_languages

        out["Languages"] = (
            aws_sdk_comprehend.types.list_of_dominant_languages.serialize_aws_json_1_1(
                value["languages"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectDominantLanguageResponse:
    out: DetectDominantLanguageResponse = {}  # type: ignore[typeddict-item]
    if "Languages" in data:
        import aws_sdk_comprehend.types.list_of_dominant_languages

        out["languages"] = (
            aws_sdk_comprehend.types.list_of_dominant_languages.deserialize_aws_json_1_1(
                data["Languages"]
            )
        )
    return out
