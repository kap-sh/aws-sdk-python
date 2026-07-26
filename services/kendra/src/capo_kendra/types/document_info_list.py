"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.document_info

DocumentInfoList: TypeAlias = list["capo_kendra.types.document_info.DocumentInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentInfoList) -> list:
    import capo_kendra.types.document_info

    out: list = []
    for item in value:
        out.append(capo_kendra.types.document_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentInfoList:
    import capo_kendra.types.document_info

    out: DocumentInfoList = []
    for item in data:
        out.append(capo_kendra.types.document_info.deserialize_aws_json_1_1(item))
    return out
