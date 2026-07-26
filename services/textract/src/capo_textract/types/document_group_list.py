"""Generated from Smithy shape ``com.amazonaws.textract#DocumentGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.document_group

DocumentGroupList: TypeAlias = list["capo_textract.types.document_group.DocumentGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentGroupList) -> list:
    import capo_textract.types.document_group

    out: list = []
    for item in value:
        out.append(capo_textract.types.document_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentGroupList:
    import capo_textract.types.document_group

    out: DocumentGroupList = []
    for item in data:
        out.append(capo_textract.types.document_group.deserialize_aws_json_1_1(item))
    return out
