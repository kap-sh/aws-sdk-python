"""Generated from Smithy shape ``com.amazonaws.kendra#FeaturedDocumentWithMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.featured_document_with_metadata

FeaturedDocumentWithMetadataList: TypeAlias = list[
    "capo_kendra.types.featured_document_with_metadata.FeaturedDocumentWithMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturedDocumentWithMetadataList) -> list:
    import capo_kendra.types.featured_document_with_metadata

    out: list = []
    for item in value:
        out.append(
            capo_kendra.types.featured_document_with_metadata.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FeaturedDocumentWithMetadataList:
    import capo_kendra.types.featured_document_with_metadata

    out: FeaturedDocumentWithMetadataList = []
    for item in data:
        out.append(
            capo_kendra.types.featured_document_with_metadata.deserialize_aws_json_1_1(
                item
            )
        )
    return out
