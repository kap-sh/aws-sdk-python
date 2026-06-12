"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectKeyPhrasesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.list_of_key_phrases


class DetectKeyPhrasesResponse(TypedDict):
    key_phrases: NotRequired[
        "aws_sdk_comprehend.types.list_of_key_phrases.ListOfKeyPhrases"
    ]
    """<p>A collection of key phrases that Amazon Comprehend identified in the input text. For each key phrase, the response provides the text of the key phrase, where the key phrase begins and ends, and the level of confidence that Amazon Comprehend has in the accuracy of the detection. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectKeyPhrasesResponse) -> dict:
    out: dict = {}
    if "key_phrases" in value:
        import aws_sdk_comprehend.types.list_of_key_phrases

        out["KeyPhrases"] = (
            aws_sdk_comprehend.types.list_of_key_phrases.serialize_aws_json_1_1(
                value["key_phrases"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectKeyPhrasesResponse:
    out: DetectKeyPhrasesResponse = {}  # type: ignore[typeddict-item]
    if "KeyPhrases" in data:
        import aws_sdk_comprehend.types.list_of_key_phrases

        out["key_phrases"] = (
            aws_sdk_comprehend.types.list_of_key_phrases.deserialize_aws_json_1_1(
                data["KeyPhrases"]
            )
        )
    return out
