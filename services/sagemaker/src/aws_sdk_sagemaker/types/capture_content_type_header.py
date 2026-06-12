"""Generated from Smithy shape ``com.amazonaws.sagemaker#CaptureContentTypeHeader``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.csv_content_types
    import aws_sdk_sagemaker.types.json_content_types


class CaptureContentTypeHeader(TypedDict):
    csv_content_types: NotRequired[
        "aws_sdk_sagemaker.types.csv_content_types.CsvContentTypes"
    ]
    """<p>The list of all content type headers that Amazon SageMaker AI will treat as CSV and capture accordingly.</p>"""
    json_content_types: NotRequired[
        "aws_sdk_sagemaker.types.json_content_types.JsonContentTypes"
    ]
    """<p>The list of all content type headers that SageMaker AI will treat as JSON and capture accordingly.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CaptureContentTypeHeader) -> dict:
    out: dict = {}
    if "csv_content_types" in value:
        import aws_sdk_sagemaker.types.csv_content_types

        out["CsvContentTypes"] = (
            aws_sdk_sagemaker.types.csv_content_types.serialize_aws_json_1_1(
                value["csv_content_types"]
            )
        )
    if "json_content_types" in value:
        import aws_sdk_sagemaker.types.json_content_types

        out["JsonContentTypes"] = (
            aws_sdk_sagemaker.types.json_content_types.serialize_aws_json_1_1(
                value["json_content_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CaptureContentTypeHeader:
    out: CaptureContentTypeHeader = {}  # type: ignore[typeddict-item]
    if "CsvContentTypes" in data:
        import aws_sdk_sagemaker.types.csv_content_types

        out["csv_content_types"] = (
            aws_sdk_sagemaker.types.csv_content_types.deserialize_aws_json_1_1(
                data["CsvContentTypes"]
            )
        )
    if "JsonContentTypes" in data:
        import aws_sdk_sagemaker.types.json_content_types

        out["json_content_types"] = (
            aws_sdk_sagemaker.types.json_content_types.deserialize_aws_json_1_1(
                data["JsonContentTypes"]
            )
        )
    return out
