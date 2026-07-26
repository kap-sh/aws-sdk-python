"""Generated from Smithy shape ``com.amazonaws.kendra#SourceDocuments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.source_document

SourceDocuments: TypeAlias = list["capo_kendra.types.source_document.SourceDocument"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceDocuments) -> list:
    import capo_kendra.types.source_document

    out: list = []
    for item in value:
        out.append(capo_kendra.types.source_document.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SourceDocuments:
    import capo_kendra.types.source_document

    out: SourceDocuments = []
    for item in data:
        out.append(capo_kendra.types.source_document.deserialize_aws_json_1_1(item))
    return out
