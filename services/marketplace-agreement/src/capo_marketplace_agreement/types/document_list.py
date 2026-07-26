"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#DocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.document_item

DocumentList: TypeAlias = list[
    "capo_marketplace_agreement.types.document_item.DocumentItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DocumentList) -> list:
    import capo_marketplace_agreement.types.document_item

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.document_item.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DocumentList:
    import capo_marketplace_agreement.types.document_item

    out: DocumentList = []
    for item in data:
        out.append(
            capo_marketplace_agreement.types.document_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
