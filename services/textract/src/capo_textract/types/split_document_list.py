"""Generated from Smithy shape ``com.amazonaws.textract#SplitDocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.split_document

SplitDocumentList: TypeAlias = list["capo_textract.types.split_document.SplitDocument"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SplitDocumentList) -> list:
    import capo_textract.types.split_document

    out: list = []
    for item in value:
        out.append(capo_textract.types.split_document.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SplitDocumentList:
    import capo_textract.types.split_document

    out: SplitDocumentList = []
    for item in data:
        out.append(capo_textract.types.split_document.deserialize_aws_json_1_1(item))
    return out
