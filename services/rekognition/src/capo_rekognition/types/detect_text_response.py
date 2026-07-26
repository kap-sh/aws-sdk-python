"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectTextResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.string
    import capo_rekognition.types.text_detection_list


class DetectTextResponse(TypedDict, closed=True):
    text_detections: NotRequired[
        "capo_rekognition.types.text_detection_list.TextDetectionList"
    ]
    """<p>An array of text that was detected in the input image.</p>"""
    text_model_version: NotRequired["capo_rekognition.types.string.String"]
    """<p>The model version used to detect text.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectTextResponse) -> dict:
    out: dict = {}
    if "text_detections" in value:
        import capo_rekognition.types.text_detection_list

        out["TextDetections"] = (
            capo_rekognition.types.text_detection_list.serialize_aws_json_1_1(
                value["text_detections"]
            )
        )
    if "text_model_version" in value:
        out["TextModelVersion"] = value["text_model_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectTextResponse:
    out: DetectTextResponse = {}  # type: ignore[typeddict-item]
    if "TextDetections" in data:
        import capo_rekognition.types.text_detection_list

        out["text_detections"] = (
            capo_rekognition.types.text_detection_list.deserialize_aws_json_1_1(
                data["TextDetections"]
            )
        )
    if "TextModelVersion" in data:
        out["text_model_version"] = data["TextModelVersion"]
    return out
