"""Generated from Smithy shape ``com.amazonaws.textract#LendingField``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.lending_detection
    import aws_sdk_textract.types.lending_detection_list
    import aws_sdk_textract.types.string


class LendingField(TypedDict):
    type: NotRequired["aws_sdk_textract.types.string.String"]
    """<p>The type of the lending document.</p>"""
    key_detection: NotRequired[
        "aws_sdk_textract.types.lending_detection.LendingDetection"
    ]
    value_detections: NotRequired[
        "aws_sdk_textract.types.lending_detection_list.LendingDetectionList"
    ]
    """<p>An array of LendingDetection objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LendingField) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "key_detection" in value:
        import aws_sdk_textract.types.lending_detection

        out["KeyDetection"] = (
            aws_sdk_textract.types.lending_detection.serialize_aws_json_1_1(
                value["key_detection"]
            )
        )
    if "value_detections" in value:
        import aws_sdk_textract.types.lending_detection_list

        out["ValueDetections"] = (
            aws_sdk_textract.types.lending_detection_list.serialize_aws_json_1_1(
                value["value_detections"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LendingField:
    out: LendingField = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "KeyDetection" in data:
        import aws_sdk_textract.types.lending_detection

        out["key_detection"] = (
            aws_sdk_textract.types.lending_detection.deserialize_aws_json_1_1(
                data["KeyDetection"]
            )
        )
    if "ValueDetections" in data:
        import aws_sdk_textract.types.lending_detection_list

        out["value_detections"] = (
            aws_sdk_textract.types.lending_detection_list.deserialize_aws_json_1_1(
                data["ValueDetections"]
            )
        )
    return out
