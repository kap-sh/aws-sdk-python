"""Generated from Smithy shape ``com.amazonaws.kendra#SourceDocuments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.source_document

SourceDocuments: TypeAlias = list["aws_sdk_kendra.types.source_document.SourceDocument"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceDocuments) -> list:
    import aws_sdk_kendra.types.source_document

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra.types.source_document.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SourceDocuments:
    import aws_sdk_kendra.types.source_document

    out: SourceDocuments = []
    for item in data:
        out.append(aws_sdk_kendra.types.source_document.deserialize_aws_json_1_1(item))
    return out
