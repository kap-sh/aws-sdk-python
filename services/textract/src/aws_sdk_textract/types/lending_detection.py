"""Generated from Smithy shape ``com.amazonaws.textract#LendingDetection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.geometry
    import aws_sdk_textract.types.percent
    import aws_sdk_textract.types.selection_status
    import aws_sdk_textract.types.string


class LendingDetection(TypedDict):
    text: NotRequired["aws_sdk_textract.types.string.String"]
    """<p>The text extracted for a detected value in a lending document.</p>"""
    selection_status: NotRequired[
        "aws_sdk_textract.types.selection_status.SelectionStatus"
    ]
    """<p>The selection status of a selection element, such as an option button or check box.</p>"""
    geometry: NotRequired["aws_sdk_textract.types.geometry.Geometry"]
    confidence: NotRequired["aws_sdk_textract.types.percent.Percent"]
    """<p>The confidence level for the text of a detected value in a lending document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LendingDetection) -> dict:
    out: dict = {}
    if "text" in value:
        out["Text"] = value["text"]
    if "selection_status" in value:
        import aws_sdk_textract.types.selection_status

        out["SelectionStatus"] = (
            aws_sdk_textract.types.selection_status.serialize_aws_json_1_1(
                value["selection_status"]
            )
        )
    if "geometry" in value:
        import aws_sdk_textract.types.geometry

        out["Geometry"] = aws_sdk_textract.types.geometry.serialize_aws_json_1_1(
            value["geometry"]
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LendingDetection:
    out: LendingDetection = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    if "SelectionStatus" in data:
        import aws_sdk_textract.types.selection_status

        out["selection_status"] = (
            aws_sdk_textract.types.selection_status.deserialize_aws_json_1_1(
                data["SelectionStatus"]
            )
        )
    if "Geometry" in data:
        import aws_sdk_textract.types.geometry

        out["geometry"] = aws_sdk_textract.types.geometry.deserialize_aws_json_1_1(
            data["Geometry"]
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    return out
