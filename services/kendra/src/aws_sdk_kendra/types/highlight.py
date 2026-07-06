"""Generated from Smithy shape ``com.amazonaws.kendra#Highlight``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.boolean
    import aws_sdk_kendra.types.highlight_type
    import aws_sdk_kendra.types.integer


class Highlight(TypedDict, closed=True):
    begin_offset: "aws_sdk_kendra.types.integer.Integer"
    """<p>The zero-based location in the response string where the highlight starts.</p>"""
    end_offset: "aws_sdk_kendra.types.integer.Integer"
    """<p>The zero-based location in the response string where the highlight ends.</p>"""
    top_answer: "aws_sdk_kendra.types.boolean.Boolean"
    """<p>Indicates whether the response is the best response. True if this is the best response; otherwise, false.</p>"""
    type: NotRequired["aws_sdk_kendra.types.highlight_type.HighlightType"]
    """<p>The highlight type. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Highlight) -> dict:
    out: dict = {}
    out["BeginOffset"] = value["begin_offset"]
    out["EndOffset"] = value["end_offset"]
    out["TopAnswer"] = value.get("top_answer", False)
    if "type" in value:
        import aws_sdk_kendra.types.highlight_type

        out["Type"] = aws_sdk_kendra.types.highlight_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Highlight:
    out: Highlight = {}  # type: ignore[typeddict-item]
    if "BeginOffset" in data:
        out["begin_offset"] = data["BeginOffset"]
    else:
        raise DeserializationError("Highlight.begin_offset required")
    if "EndOffset" in data:
        out["end_offset"] = data["EndOffset"]
    else:
        raise DeserializationError("Highlight.end_offset required")
    if "TopAnswer" in data:
        out["top_answer"] = data["TopAnswer"]
    else:
        out["top_answer"] = False
    if "Type" in data:
        import aws_sdk_kendra.types.highlight_type

        out["type"] = aws_sdk_kendra.types.highlight_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out
