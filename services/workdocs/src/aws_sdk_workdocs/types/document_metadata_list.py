"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.document_metadata

DocumentMetadataList: TypeAlias = list[
    "aws_sdk_workdocs.types.document_metadata.DocumentMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentMetadataList) -> list:
    import aws_sdk_workdocs.types.document_metadata

    out: list = []
    for item in value:
        out.append(aws_sdk_workdocs.types.document_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> DocumentMetadataList:
    import aws_sdk_workdocs.types.document_metadata

    out: DocumentMetadataList = []
    for item in data:
        out.append(aws_sdk_workdocs.types.document_metadata.deserialize_json(item))
    return out
