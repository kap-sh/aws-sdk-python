"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentVersionMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.document_version_metadata

DocumentVersionMetadataList: TypeAlias = list[
    "aws_sdk_workdocs.types.document_version_metadata.DocumentVersionMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentVersionMetadataList) -> list:
    import aws_sdk_workdocs.types.document_version_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workdocs.types.document_version_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DocumentVersionMetadataList:
    import aws_sdk_workdocs.types.document_version_metadata

    out: DocumentVersionMetadataList = []
    for item in data:
        out.append(
            aws_sdk_workdocs.types.document_version_metadata.deserialize_json(item)
        )
    return out
