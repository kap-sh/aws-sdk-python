"""Generated from Smithy shape ``com.amazonaws.textract#LendingResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.extraction_list
    import aws_sdk_textract.types.page_classification
    import aws_sdk_textract.types.u_integer


class LendingResult(TypedDict):
    page: NotRequired["aws_sdk_textract.types.u_integer.UInteger"]
    """<p>The page number for a page, with regard to whole submission.</p>"""
    page_classification: NotRequired[
        "aws_sdk_textract.types.page_classification.PageClassification"
    ]
    """<p>The classifier result for a given page.</p>"""
    extractions: NotRequired["aws_sdk_textract.types.extraction_list.ExtractionList"]
    """<p>An array of Extraction to hold structured data. e.g. normalized key value pairs instead of raw OCR detections .</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LendingResult) -> dict:
    out: dict = {}
    if "page" in value:
        out["Page"] = value["page"]
    if "page_classification" in value:
        import aws_sdk_textract.types.page_classification

        out["PageClassification"] = (
            aws_sdk_textract.types.page_classification.serialize_aws_json_1_1(
                value["page_classification"]
            )
        )
    if "extractions" in value:
        import aws_sdk_textract.types.extraction_list

        out["Extractions"] = (
            aws_sdk_textract.types.extraction_list.serialize_aws_json_1_1(
                value["extractions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LendingResult:
    out: LendingResult = {}  # type: ignore[typeddict-item]
    if "Page" in data:
        out["page"] = data["Page"]
    if "PageClassification" in data:
        import aws_sdk_textract.types.page_classification

        out["page_classification"] = (
            aws_sdk_textract.types.page_classification.deserialize_aws_json_1_1(
                data["PageClassification"]
            )
        )
    if "Extractions" in data:
        import aws_sdk_textract.types.extraction_list

        out["extractions"] = (
            aws_sdk_textract.types.extraction_list.deserialize_aws_json_1_1(
                data["Extractions"]
            )
        )
    return out
