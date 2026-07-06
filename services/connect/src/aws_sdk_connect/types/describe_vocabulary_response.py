"""Generated from Smithy shape ``com.amazonaws.connect#DescribeVocabularyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.vocabulary


class DescribeVocabularyResponse(TypedDict, closed=True):
    vocabulary: "aws_sdk_connect.types.vocabulary.Vocabulary"
    """<p>A list of specific words that you want Contact Lens for Connect Customer to recognize in your audio input. They are generally domain-specific words and phrases, words that Contact Lens is not recognizing, or proper nouns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVocabularyResponse) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.vocabulary

    out["Vocabulary"] = aws_sdk_connect.types.vocabulary.serialize_json(
        value["vocabulary"]
    )
    return out


def deserialize_json(data: dict) -> DescribeVocabularyResponse:
    out: DescribeVocabularyResponse = {}  # type: ignore[typeddict-item]
    if "Vocabulary" in data:
        import aws_sdk_connect.types.vocabulary

        out["vocabulary"] = aws_sdk_connect.types.vocabulary.deserialize_json(
            data["Vocabulary"]
        )
    else:
        raise DeserializationError("DescribeVocabularyResponse.vocabulary required")
    return out
