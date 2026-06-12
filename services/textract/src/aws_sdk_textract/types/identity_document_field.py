"""Generated from Smithy shape ``com.amazonaws.textract#IdentityDocumentField``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.analyze_id_detections


class IdentityDocumentField(TypedDict):
    type: NotRequired[
        "aws_sdk_textract.types.analyze_id_detections.AnalyzeIDDetections"
    ]
    value_detection: NotRequired[
        "aws_sdk_textract.types.analyze_id_detections.AnalyzeIDDetections"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityDocumentField) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_textract.types.analyze_id_detections

        out["Type"] = (
            aws_sdk_textract.types.analyze_id_detections.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "value_detection" in value:
        import aws_sdk_textract.types.analyze_id_detections

        out["ValueDetection"] = (
            aws_sdk_textract.types.analyze_id_detections.serialize_aws_json_1_1(
                value["value_detection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IdentityDocumentField:
    out: IdentityDocumentField = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_textract.types.analyze_id_detections

        out["type"] = (
            aws_sdk_textract.types.analyze_id_detections.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "ValueDetection" in data:
        import aws_sdk_textract.types.analyze_id_detections

        out["value_detection"] = (
            aws_sdk_textract.types.analyze_id_detections.deserialize_aws_json_1_1(
                data["ValueDetection"]
            )
        )
    return out
