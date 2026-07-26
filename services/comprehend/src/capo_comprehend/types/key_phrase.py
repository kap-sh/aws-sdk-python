"""Generated from Smithy shape ``com.amazonaws.comprehend#KeyPhrase``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.float
    import capo_comprehend.types.integer
    import capo_comprehend.types.string


class KeyPhrase(TypedDict, closed=True):
    score: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of the detection.</p>"""
    text: NotRequired["capo_comprehend.types.string.String"]
    """<p>The text of a key noun phrase.</p>"""
    begin_offset: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The zero-based offset from the beginning of the source text to the first character in the key phrase.</p>"""
    end_offset: NotRequired["capo_comprehend.types.integer.Integer"]
    """<p>The zero-based offset from the beginning of the source text to the last character in the key phrase.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyPhrase) -> dict:
    out: dict = {}
    if "score" in value:
        out["Score"] = value["score"]
    if "text" in value:
        out["Text"] = value["text"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KeyPhrase:
    out: KeyPhrase = {}  # type: ignore[typeddict-item]
    if "Score" in data:
        out["score"] = data["Score"]
    if "Text" in data:
        out["text"] = data["Text"]
    if "BeginOffset" in data:
        out["begin_offset"] = data["BeginOffset"]
    if "EndOffset" in data:
        out["end_offset"] = data["EndOffset"]
    return out
