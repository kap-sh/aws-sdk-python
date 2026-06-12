"""Generated from Smithy shape ``com.amazonaws.textract#LendingDocument``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.lending_field_list
    import aws_sdk_textract.types.signature_detection_list


class LendingDocument(TypedDict):
    lending_fields: NotRequired[
        "aws_sdk_textract.types.lending_field_list.LendingFieldList"
    ]
    """<p>An array of LendingField objects.</p>"""
    signature_detections: NotRequired[
        "aws_sdk_textract.types.signature_detection_list.SignatureDetectionList"
    ]
    """<p>A list of signatures detected in a lending document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LendingDocument) -> dict:
    out: dict = {}
    if "lending_fields" in value:
        import aws_sdk_textract.types.lending_field_list

        out["LendingFields"] = (
            aws_sdk_textract.types.lending_field_list.serialize_aws_json_1_1(
                value["lending_fields"]
            )
        )
    if "signature_detections" in value:
        import aws_sdk_textract.types.signature_detection_list

        out["SignatureDetections"] = (
            aws_sdk_textract.types.signature_detection_list.serialize_aws_json_1_1(
                value["signature_detections"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LendingDocument:
    out: LendingDocument = {}  # type: ignore[typeddict-item]
    if "LendingFields" in data:
        import aws_sdk_textract.types.lending_field_list

        out["lending_fields"] = (
            aws_sdk_textract.types.lending_field_list.deserialize_aws_json_1_1(
                data["LendingFields"]
            )
        )
    if "SignatureDetections" in data:
        import aws_sdk_textract.types.signature_detection_list

        out["signature_detections"] = (
            aws_sdk_textract.types.signature_detection_list.deserialize_aws_json_1_1(
                data["SignatureDetections"]
            )
        )
    return out
