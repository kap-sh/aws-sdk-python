"""Generated from Smithy shape ``com.amazonaws.comprehend#PartOfSpeechTag``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.float
    import aws_sdk_comprehend.types.part_of_speech_tag_type


class PartOfSpeechTag(TypedDict):
    tag: NotRequired[
        "aws_sdk_comprehend.types.part_of_speech_tag_type.PartOfSpeechTagType"
    ]
    """<p>Identifies the part of speech that the token represents.</p>"""
    score: NotRequired["aws_sdk_comprehend.types.float.Float"]
    """<p>The confidence that Amazon Comprehend has that the part of speech was correctly identified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartOfSpeechTag) -> dict:
    out: dict = {}
    if "tag" in value:
        import aws_sdk_comprehend.types.part_of_speech_tag_type

        out["Tag"] = (
            aws_sdk_comprehend.types.part_of_speech_tag_type.serialize_aws_json_1_1(
                value["tag"]
            )
        )
    if "score" in value:
        out["Score"] = value["score"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PartOfSpeechTag:
    out: PartOfSpeechTag = {}  # type: ignore[typeddict-item]
    if "Tag" in data:
        import aws_sdk_comprehend.types.part_of_speech_tag_type

        out["tag"] = (
            aws_sdk_comprehend.types.part_of_speech_tag_type.deserialize_aws_json_1_1(
                data["Tag"]
            )
        )
    if "Score" in data:
        out["score"] = data["Score"]
    return out
