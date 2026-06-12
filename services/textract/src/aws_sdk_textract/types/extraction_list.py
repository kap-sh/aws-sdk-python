"""Generated from Smithy shape ``com.amazonaws.textract#ExtractionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_textract.types.extraction

ExtractionList: TypeAlias = list["aws_sdk_textract.types.extraction.Extraction"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtractionList) -> list:
    import aws_sdk_textract.types.extraction

    out: list = []
    for item in value:
        out.append(aws_sdk_textract.types.extraction.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExtractionList:
    import aws_sdk_textract.types.extraction

    out: ExtractionList = []
    for item in data:
        out.append(aws_sdk_textract.types.extraction.deserialize_aws_json_1_1(item))
    return out
