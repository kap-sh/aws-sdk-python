"""Generated from Smithy shape ``com.amazonaws.kendra#FeaturedDocumentMissingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.featured_document_missing

FeaturedDocumentMissingList: TypeAlias = list[
    "capo_kendra.types.featured_document_missing.FeaturedDocumentMissing"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturedDocumentMissingList) -> list:
    import capo_kendra.types.featured_document_missing

    out: list = []
    for item in value:
        out.append(
            capo_kendra.types.featured_document_missing.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FeaturedDocumentMissingList:
    import capo_kendra.types.featured_document_missing

    out: FeaturedDocumentMissingList = []
    for item in data:
        out.append(
            capo_kendra.types.featured_document_missing.deserialize_aws_json_1_1(item)
        )
    return out
