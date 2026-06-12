"""Generated from Smithy shape ``com.amazonaws.rekognition#SegmentTypeInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.segment_type
    import aws_sdk_rekognition.types.string


class SegmentTypeInfo(TypedDict):
    type: NotRequired["aws_sdk_rekognition.types.segment_type.SegmentType"]
    """<p>The type of a segment (technical cue or shot detection).</p>"""
    model_version: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>The version of the model used to detect segments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SegmentTypeInfo) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_rekognition.types.segment_type

        out["Type"] = aws_sdk_rekognition.types.segment_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SegmentTypeInfo:
    out: SegmentTypeInfo = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_rekognition.types.segment_type

        out["type"] = aws_sdk_rekognition.types.segment_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "ModelVersion" in data:
        out["model_version"] = data["ModelVersion"]
    return out
