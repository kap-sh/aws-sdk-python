"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.document

DocumentList: TypeAlias = list["capo_kendra.types.document.Document"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentList) -> list:
    import capo_kendra.types.document

    out: list = []
    for item in value:
        out.append(capo_kendra.types.document.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentList:
    import capo_kendra.types.document

    out: DocumentList = []
    for item in data:
        out.append(capo_kendra.types.document.deserialize_aws_json_1_1(item))
    return out
