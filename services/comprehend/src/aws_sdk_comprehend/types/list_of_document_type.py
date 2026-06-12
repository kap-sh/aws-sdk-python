"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfDocumentType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.document_type_list_item

ListOfDocumentType: TypeAlias = list[
    "aws_sdk_comprehend.types.document_type_list_item.DocumentTypeListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfDocumentType) -> list:
    import aws_sdk_comprehend.types.document_type_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.document_type_list_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfDocumentType:
    import aws_sdk_comprehend.types.document_type_list_item

    out: ListOfDocumentType = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.document_type_list_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out
