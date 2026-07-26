"""Generated from Smithy shape ``com.amazonaws.kendra#FeaturedDocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.featured_document

FeaturedDocumentList: TypeAlias = list[
    "capo_kendra.types.featured_document.FeaturedDocument"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturedDocumentList) -> list:
    import capo_kendra.types.featured_document

    out: list = []
    for item in value:
        out.append(capo_kendra.types.featured_document.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FeaturedDocumentList:
    import capo_kendra.types.featured_document

    out: FeaturedDocumentList = []
    for item in data:
        out.append(capo_kendra.types.featured_document.deserialize_aws_json_1_1(item))
    return out
